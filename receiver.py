"""Set the Environment Information Needed to Access Your Lab!

The provided sample code in this repository will reference this file to get the
information needed to connect to your lab backend.  You provide this info here
once and the scripts in this repository will access it as needed by the lab.


Copyright (c) 2018 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Libraries
from pprint import pprint
from flask import Flask, json, request, render_template
import sys, os, getopt, json
from webexteamssdk import WebexTeamsAPI
import adaptive_cards
import snapshot_card
import open_door_card
import door_timer_card
import requests
import meraki
import time
import shutil
import datetime
import pymsteams

# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))

# Get the absolute path for the project / repository root
project_root = os.path.abspath(os.path.join(here, ".."))

# Extend the system path to include the project root and import the env files
sys.path.insert(0, project_root)
import credentials  # noqa

# WEBEX TEAMS CLIENT
teamsapi = WebexTeamsAPI(access_token=credentials.WT_ACCESS_TOKEN)
# MERAKI DASHBOARD API CLIENT
dashboard = meraki.DashboardAPI(
			api_key=credentials.MERAKI_API_KEY,
			base_url=credentials.MERAKI_BASEURL,
			print_console=False)
# MS URL
msteamsurl = credentials.MS_TEAMS_URL

# Flask App
app = Flask(__name__)

# Webhook Receiver Code - Accepts JSON POST from Meraki and
# Posts to WebEx Teams
@app.route("/", methods=["POST"])
def get_webhook_json():
    global webhook_data
    global seen_alerts
    start_time = time.time()
    threshold_time = 60

    # Webhook Receiver
    webhook_data_json = request.json
    pprint(webhook_data_json, indent=1)
    webhook_data = json.dumps(webhook_data_json)
    # WebEx Teams can only handle so much text so limit to 1000 chars
    webhook_data = webhook_data[:1000] + '...'

    # Gather Alert Data
    alert_data = []
    alert_type = webhook_data_json['alertType']
    alert_id = webhook_data_json['alertId']
    organization_name = webhook_data_json['organizationName']
    network_name = webhook_data_json['networkName']
    network_id = webhook_data_json['networkId']
    alert_data.extend([alert_type, alert_id, organization_name, network_name])
    timestamp = webhook_data_json['occurredAt']


    #Avoid duplicate Alert IDs
    if alert_id not in seen_alerts:
        seen_alerts.append(alert_id)

        #Workflow for Sensors
        if alert_type == 'Sensor change detected':
            sensor_value = webhook_data_json['alertData']['triggerData'][0]['trigger']['sensorValue']
            device_model = webhook_data_json['deviceModel']
            device_name = webhook_data_json['deviceName']
            device_serial = webhook_data_json['deviceSerial']
            device_url = webhook_data_json['deviceUrl']
            alert_ts = webhook_data_json['alertData']['triggerData'][0]['trigger']['ts']
            alert_data.extend([sensor_value, device_model, device_name])

            #Workflow for door sensor with Snapshot API
            if device_model == 'MT20' and sensor_value == 1.0:
                card = adaptive_cards.open_door_card(
                    network_name=network_name,
                    sensor_name=device_name,
                    model_name=device_model,
                    sensor_link=device_url,
                    timestamp=str(datetime.datetime.fromtimestamp(alert_ts))
                    )
                # Send Adaptive Card to Webex Teams
                msg = teamsapi.messages.create(
                    credentials.WT_ROOM_ID,
                    text='fallback',
                    attachments=[card]
                )

                # Send Adaptive Card to MS Teams
                send_msteams_card(card=card, url= msteamsurl)

                # Save msg ID to start thread with Snapshot
                msg_id = msg.id
                # Snapshot timestamp must be in ISO format
                iso_ts = datetime.datetime.utcfromtimestamp(alert_ts).isoformat() + 'Z'

                # Snapshots referenced with timestamps may take a minute to be available
                # During which fetching will likely fail
                # This loops 4 times or exits
                i = 0
                while i < 5:
                    try:
                        print('Fetching camera snapshot...')
                        snapshot = dashboard.camera.generateDeviceCameraSnapshot(
                            serial=credentials.MERAKI_CAMS[0], timestamp=iso_ts)
                    except meraki.exceptions.APIError:
                        time.sleep(30)
                        i = i + 1
                        if i == 5:
                            print('Failed to fetch camera snapshot.')
                        continue
                    break
                # Get camera data
                camera = dashboard.devices.getDevice(
                    serial=credentials.MERAKI_CAMS[0]
                )

                card = adaptive_cards.snapshot_card(
                    network_name=network_name,
                    camera_name=camera['name'],
                    model_name=camera['model'],
                    timestamp=str(datetime.datetime.fromtimestamp(alert_ts)),
                    camera_link=camera['url'],
                    snapshot_link=snapshot['url']
                )

                teamsapi.messages.create(
                    credentials.WT_ROOM_ID,
                    text='fallback', attachments=[card], parentId=msg_id
                )

                # Send Adaptive Card to MS Teams
                send_msteams_card(card=card, url= msteamsurl)

                #Workflow for time based alerting
                elapsed_time = time.time()-start_time
                if elapsed_time < threshold_time:
                    time_to_go = threshold_time - elapsed_time
                    time.sleep(time_to_go)

                url = f'https://api.meraki.com/api/v1/networks/{network_id}/sensors/stats/latestBySensor?metric=door&serials[]={device_serial}'
                payload = None
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": f'{credentials.MERAKI_API_KEY}'
                }

                response = requests.request('GET', url, headers=headers, data = payload)

                elapsed_time = "{:.2f}".format(time.time()-start_time)
                if json.loads(response.text)[0]['value']==1.0:
                    card = adaptive_cards.door_timer_card(
                        network_name=network_name,
                        model_name=device_model,
                        sensor_name=device_name,
                        timestamp=str(datetime.datetime.fromtimestamp(json.loads(response.text)[0]['timestamp'])),
                        sensor_link=device_url,
                        elapsed_time=elapsed_time
                    )

                    teamsapi.messages.create(
                    credentials.WT_ROOM_ID,
                    text='fallback', parentId=msg_id, attachments=[card]
                )

                # Send Adaptive Card to MS Teams
                send_msteams_card(card=card, url= msteamsurl)

        """
        if alert_type == 'Motion detected':
            image_url = webhook_data_json['alertData']['imageUrl']
            camera_name = webhook_data_json['deviceName']
            camera_url = webhook_data_json['deviceUrl']
            alert_ts = webhook_data_json['alertData']['timestamp']
            timestr = time.ctime(alert_ts)
            print(timestr)
            time.sleep(5)
            print('Storing snapshot locally...')
            resp = requests.get(image_url, stream=True)
            filename = f'./snaps/motion_detected_{timestr}.jpg'
            local_file = open(filename, 'wb')
            resp.raw.decode_content = True
            shutil.copyfileobj(resp.raw, local_file)
            local_file.close()
            teamsapi.messages.create(
                credentials.WT_ROOM_ID,
                text="Meraki Webhook Alert: Motion detected for camera " + network_name + " - " +
                    camera_name + " - " + camera_url, files=[filename]
            )
            """


        # Uncomment if you want to get the alert data for any other alerts in your chat
        #else:
        #    teamsapi.messages.create(
        #        credentials.WT_ROOM_ID,
        #        text="Meraki Webhook Alert: " + webhook_data
        #    )
        #print(alert_data)

        # Return success message

    return "WebHook POST Received"

# Launch application with supplied arguments
def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hs:", ["secret="])
    except getopt.GetoptError:
        print("receiver.py -s <secret>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("receiver.py -s <secret>")
            sys.exit()
        elif opt in ("-s", "--secret"):
            secret = arg

    print("secret: " + secret)

def send_msteams_card(card,url):
    card_msteams = {
        "type":"message",
        "attachments":[card]
    }
    msteams_payload = json.dumps(card_msteams)
    msteams_headers = {
        "Content-Type": "application/json"
    }
    msteams_msg = requests.request('POST', msteamsurl, headers=msteams_headers, data=msteams_payload)


if __name__ == "__main__":
    seen_alerts = []
    main(sys.argv[1:])
    app.run(host="0.0.0.0", port=5005, debug=False)
