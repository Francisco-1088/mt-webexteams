def open_door(network_name, model_name, sensor_name, timestamp, sensor_link):
    card = {
        "blocks": [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://png.pngitem.com/pimgs/s/367-3673410_door-alarm-door-alarm-icon-transparent-hd-png.png",
                        "alt_text": "images"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Open Door Detected!*"
                    }
                ]
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*Network Name:*"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f'{network_name}'
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Sensor Name:*"
                    },
                    {
                        "type": "plain_text",
                        "text": f'{sensor_name}'
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Model:*"
                    },
                    {
                        "type": "plain_text",
                        "text": f'{model_name}'
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Timestamp:*"
                    },
                    {
                        "type": "plain_text",
                        "text": f'{timestamp}'
                    }
                ]
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://developer.webex.com/images/link-icon.png",
                        "alt_text": "images"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"<{sensor_link}|Go to Dashboard Sensor Link>"
                    }
                ]
            }
        ]
    }

    return card

def snapshot_card(network_name, camera_name, model_name, timestamp, camera_link, snapshot_link):
    card = {
        "blocks": [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRspxoQVhoPY_NuCw3-7nPybL_RXJX7STwOOg&usqp=CAU",
                        "alt_text": "images"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Meraki MV Snapshot*"
                    }
                ]
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*Network Name:*"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"{network_name}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Camera Name:*"
                    },
                    {
                        "type": "plain_text",
                        "text": f"{camera_name}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Model:*"
                    },
                    {
                        "type": "plain_text",
                        "text": f"{model_name}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Timestamp:*"
                    },
                    {
                        "type": "plain_text",
                        "text": f"{timestamp}"
                    }
                ]
            },
            {
                "type": "image",
                "image_url": f"{snapshot_link}",
                "alt_text": "Camera Snapshot."
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://developer.webex.com/images/link-icon.png",
                        "alt_text": "images"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"<{camera_link}|Go to Dashboard Camera Link>"
                    }
                ]
            }
        ]
    }

    return card

def door_left_open_card(network_name, model_name, sensor_name, timestamp, sensor_link, elapsed_time):
    card = {
        "blocks": [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://miro.medium.com/max/952/1*TbjqUyHNDTGMdl5LOuyf1w.png",
                        "alt_text": "images"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Door open for too long!*"
                    }
                ]
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*Network Name:*"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"{network_name}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Sensor Name:*"
                    },
                    {
                        "type": "plain_text",
                        "text": f"{sensor_name}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Model:*"
                    },
                    {
                        "type": "plain_text",
                        "text": f"{model_name}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Initial Alert:*"
                    },
                    {
                        "type": "plain_text",
                        "text": f"{timestamp}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Alerting for:*"
                    },
                    {
                        "type": "plain_text",
                        "text": f"{elapsed_time}"
                    }
                ]
            },
            {
                "type": "image",
                "image_url": "https://meraki-us-west-2-test-devel.s3.us-west-2.amazonaws.com/sp/vf/motion_images/647955396387938455/1612753956.064.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJT4Y6MIN4RDUITNQ%2F20210208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210208T031932Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=f433fc207532e4953be93e7bdd7ccff8f5757823f971840edb03944b48a2fbcd",
                "alt_text": "Camera Snapshot."
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://developer.webex.com/images/link-icon.png",
                        "alt_text": "images"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"<{sensor_link}|Go to Dashboard Sensor Link>"
                    }
                ]
            }
        ]
    }

    return card

def motion_recap_card(network_name, camera_name, model_name, sensor_name, timestamp, camera_link, snapshot_link, sensor_link):
    card = {
        "blocks": [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://png.pngitem.com/pimgs/s/367-3673410_door-alarm-door-alarm-icon-transparent-hd-png.png",
                        "alt_text": "images"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Open Door Detected!*"
                    }
                ]
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*Network Name:*"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"{network_name}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Camera Name:*"
                    },
                    {
                        "type": "plain_text",
                        "text": f"{camera_name}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Sensor Name:*"
                    },
                    {
                        "type": "plain_text",
                        "text": f"{sensor_name}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Camera Model:*"
                    },
                    {
                        "type": "plain_text",
                        "text": f"{model_name}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Timestamp:*"
                    },
                    {
                        "type": "plain_text",
                        "text": f"{timestamp}"
                    }
                ]
            },
            {
                "type": "image",
                "image_url": f"{snapshot_link}",
                "alt_text": "Camera Snapshot."
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://developer.webex.com/images/link-icon.png",
                        "alt_text": "images"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"<{camera_link}|Go to Dashboard Camera Link>"
                    }
                ]
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://developer.webex.com/images/link-icon.png",
                        "alt_text": "images"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"<{sensor_link}|Go to Dashboard Sensor Link>"
                    }
                ]
            }
        ]
    }

    return card