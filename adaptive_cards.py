def open_door_cardv2(network_name, model_name, sensor_name, timestamp, sensor_link, snapshot_link=None, video_link=None):
    card = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "body": [
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "Image",
                                    "style": "Person",
                                    "url": "https://assets.brandfolder.com/2pkq94n2vgcgj3fs2p8x2x/v/52445274/original/topology-icon-mt10-small.png",
                                    "size": "Medium",
                                    "height": "50px"
                                }
                            ],
                            "width": "auto"
                        },
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Meraki Dashboard Alert",
                                    "weight": "Lighter",
                                    "color": "Accent"
                                },
                                {
                                    "type": "TextBlock",
                                    "weight": "Bolder",
                                    "text": "Open Door Detected!",
                                    "horizontalAlignment": "Left",
                                    "wrap": True,
                                    "color": "default",
                                    "size": "Large",
                                    "spacing": "Small"
                                }
                            ],
                            "width": "stretch"
                        }
                    ]
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": 35,
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Network Name:",
                                    "weight": "Bolder",
                                    "color": "default"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Sensor Name:",
                                    "weight": "Bolder",
                                    "color": "default",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Model:",
                                    "weight": "Bolder",
                                    "color": "default",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Timestamp:",
                                    "weight": "Bolder",
                                    "color": "default",
                                    "spacing": "Small"
                                }
                            ]
                        },
                        {
                            "type": "Column",
                            "width": 65,
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": network_name,
                                    "color": "default"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": f"[{sensor_name}]({sensor_link})",
                                    "color": "default",
                                    "weight": "Lighter",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": model_name,
                                    "weight": "Lighter",
                                    "color": "default",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": timestamp,
                                    "weight": "Lighter",
                                    "color": "default",
                                    "spacing": "Small"
                                }
                            ]
                        }
                    ],
                    "spacing": "Padding",
                    "horizontalAlignment": "Center"
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "Image",
                                    "altText": "",
                                    "url": "https://assets.brandfolder.com/hmrg83gh2p6wsmjbxvhfhtgx/v/52451031/original/topology-icon-mv12-small.png",
                                    "size": "Small",
                                    "width": "15px"
                                },
                                {
                                    "type": "Image",
                                    "altText": "",
                                    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbNqWSFeDK2U7l8x8vT4xT_7bpGG0T4-V8rQ&usqp=CAU",
                                    "size": "Small",
                                    "width": "15px"
                                }
                            ],
                            "spacing": "Small"
                        },
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": f"[Go to Camera Snapshot Link]({snapshot_link})",
                                    "horizontalAlignment": "Left",
                                    "size": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": f"[Go to Camera Video Link]({video_link})",
                                    "horizontalAlignment": "Left",
                                    "size": "Small"
                                }
                            ],
                            "verticalContentAlignment": "Center",
                            "horizontalAlignment": "Left",
                            "spacing": "Large"
                        }
                    ]
                }
            ],
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "version": "1.2"
        }
    }

    return card

def open_door_card(network_name, model_name, sensor_name, timestamp, sensor_link):
    card = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.2",
            "body": [
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "Image",
                                    "style": "Person",
                                    "url": "https://png.pngitem.com/pimgs/s/367-3673410_door-alarm-door-alarm-icon-transparent-hd-png.png",
                                    "size": "Medium",
                                    "height": "50px"
                                }
                            ],
                            "width": "auto"
                        },
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Meraki Dashboard Alert",
                                    "weight": "Lighter",
                                    "color": "Accent"
                                },
                                {
                                    "type": "TextBlock",
                                    "weight": "Bolder",
                                    "text": "Open Door Detected!",
                                    "horizontalAlignment": "Left",
                                    "wrap": True,
                                    "color": "default",
                                    "size": "Large",
                                    "spacing": "Small"
                                }
                            ],
                            "width": "stretch"
                        }
                    ]
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": 35,
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Network Name:",
                                    "weight": "Bolder",
                                    "color": "default"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Sensor Name:",
                                    "weight": "Bolder",
                                    "color": "default",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Model:",
                                    "weight": "Bolder",
                                    "color": "default",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Timestamp:",
                                    "weight": "Bolder",
                                    "color": "default",
                                    "spacing": "Small"
                                }
                            ]
                        },
                        {
                            "type": "Column",
                            "width": 65,
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": network_name,
                                    "color": "default"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": sensor_name,
                                    "color": "default",
                                    "weight": "Lighter",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": model_name,
                                    "weight": "Lighter",
                                    "color": "default",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": timestamp,
                                    "weight": "Lighter",
                                    "color": "default",
                                    "spacing": "Small"
                                }
                            ]
                        }
                    ],
                    "spacing": "Padding",
                    "horizontalAlignment": "Center"
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "Image",
                                    "altText": "",
                                    "url": "https://developer.webex.com/images/link-icon.png",
                                    "size": "Small",
                                    "width": "30px"
                                }
                            ],
                            "spacing": "Small"
                        },
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": f"[Go to Sensor Dashboard Link]({sensor_link})",
                                    "horizontalAlignment": "Left",
                                    "size": "Medium"
                                }
                            ],
                            "verticalContentAlignment": "Center",
                            "horizontalAlignment": "Left",
                            "spacing": "Small"
                        }
                    ]
                }
            ]
        }
    }

    return card

def snapshot_card(network_name, camera_name, model_name, timestamp, camera_link, snapshot_link):
    card = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.2",
            "body": [
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "Image",
                                    "style": "Person",
                                    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRspxoQVhoPY_NuCw3-7nPybL_RXJX7STwOOg&usqp=CAU",
                                    "size": "Medium",
                                    "height": "50px"
                                }
                            ],
                            "width": "auto"
                        },
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Meraki Dashboard Alert",
                                    "weight": "Lighter",
                                    "color": "Accent"
                                },
                                {
                                    "type": "TextBlock",
                                    "weight": "Bolder",
                                    "text": "Meraki MV Snapshot",
                                    "horizontalAlignment": "Left",
                                    "wrap": True,
                                    "color": "default",
                                    "size": "Large",
                                    "spacing": "Small"
                                }
                            ],
                            "width": "stretch"
                        }
                    ]
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": 35,
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Network Name:",
                                    "weight": "Bolder",
                                    "color": "default"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Camera Name:",
                                    "weight": "Bolder",
                                    "color": "default",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Model:",
                                    "weight": "Bolder",
                                    "color": "default",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Timestamp:",
                                    "weight": "Bolder",
                                    "color": "default",
                                    "spacing": "Small"
                                }
                            ]
                        },
                        {
                            "type": "Column",
                            "width": 65,
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": network_name,
                                    "color": "default"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": camera_name,
                                    "color": "default",
                                    "weight": "Lighter",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": model_name,
                                    "weight": "Lighter",
                                    "color": "default",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": timestamp,
                                    "weight": "Lighter",
                                    "color": "default",
                                    "spacing": "Small"
                                }
                            ]
                        }
                    ],
                    "spacing": "Padding",
                    "horizontalAlignment": "Center"
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "Image",
                                    "url": snapshot_link
                                }
                            ]
                        }
                    ],
                    "spacing": "Padding",
                    "horizontalAlignment": "Center"
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "Image",
                                    "altText": "",
                                    "url": "https://developer.webex.com/images/link-icon.png",
                                    "size": "Small",
                                    "width": "30px"
                                }
                            ],
                            "spacing": "Small"
                        },
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": f"[Go to Camera Dashboard Link]({camera_link})",
                                    "horizontalAlignment": "Left",
                                    "size": "Medium"
                                }
                            ],
                            "verticalContentAlignment": "Center",
                            "horizontalAlignment": "Left",
                            "spacing": "Small"
                        }
                    ]
                }
            ]
        }
    }

    return card

def door_timer_card(network_name, model_name, sensor_name, timestamp, sensor_link, elapsed_time):
    card = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.2",
            "body": [
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "Image",
                                    "style": "Person",
                                    "url": "https://miro.medium.com/max/952/1*TbjqUyHNDTGMdl5LOuyf1w.png",
                                    "size": "Medium",
                                    "height": "50px"
                                }
                            ],
                            "width": "auto"
                        },
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Meraki Dashboard Alert",
                                    "weight": "Lighter",
                                    "color": "Accent"
                                },
                                {
                                    "type": "TextBlock",
                                    "weight": "Bolder",
                                    "text": "Door open for too long!",
                                    "horizontalAlignment": "Left",
                                    "wrap": True,
                                    "color": "default",
                                    "size": "Large",
                                    "spacing": "Small"
                                }
                            ],
                            "width": "stretch"
                        }
                    ]
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": 35,
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Network Name:",
                                    "weight": "Bolder",
                                    "color": "default"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Sensor Name:",
                                    "weight": "Bolder",
                                    "color": "default",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Model:",
                                    "weight": "Bolder",
                                    "color": "default",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Initial Alert:",
                                    "weight": "Bolder",
                                    "color": "default",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Alerting for:",
                                    "weight": "Bolder",
                                    "color": "default",
                                    "spacing": "Small"
                                }
                            ]
                        },
                        {
                            "type": "Column",
                            "width": 65,
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": network_name,
                                    "color": "default"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": sensor_name,
                                    "color": "default",
                                    "weight": "Lighter",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": model_name,
                                    "weight": "Lighter",
                                    "color": "default",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": timestamp,
                                    "weight": "Lighter",
                                    "color": "default",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": f'{elapsed_time} seconds',
                                    "weight": "Lighter",
                                    "color": "default",
                                    "spacing": "Small"
                                }
                            ]
                        }
                    ],
                    "spacing": "Padding",
                    "horizontalAlignment": "Center"
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "Image",
                                    "altText": "",
                                    "url": "https://developer.webex.com/images/link-icon.png",
                                    "size": "Small",
                                    "width": "30px"
                                }
                            ],
                            "spacing": "Small"
                        },
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": f'[Go to Sensor Dashboard Link]({sensor_link})',
                                    "horizontalAlignment": "Left",
                                    "size": "Medium"
                                }
                            ],
                            "verticalContentAlignment": "Center",
                            "horizontalAlignment": "Left",
                            "spacing": "Small"
                        }
                    ]
                }
            ]
        }
    }

    return card


def combo_card(network_name, camera_name, model_name, sensor_name, timestamp, camera_link, snapshot_link, sensor_link):
    card = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.2",
            "body": [
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "Image",
                                    "style": "Person",
                                    "url": "https://png.pngitem.com/pimgs/s/367-3673410_door-alarm-door-alarm-icon-transparent-hd-png.png",
                                    "size": "Medium",
                                    "height": "50px"
                                }
                            ],
                            "width": "auto"
                        },
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Meraki Dashboard Alert",
                                    "weight": "Lighter",
                                    "color": "Accent"
                                },
                                {
                                    "type": "TextBlock",
                                    "weight": "Bolder",
                                    "text": "Open Door Detected!",
                                    "horizontalAlignment": "Left",
                                    "wrap": True,
                                    "color": "default",
                                    "size": "Large",
                                    "spacing": "Small"
                                }
                            ],
                            "width": "stretch"
                        }
                    ]
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": 35,
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Network Name:",
                                    "weight": "Bolder",
                                    "color": "default"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Camera Name:",
                                    "weight": "Bolder",
                                    "color": "default",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Sensor Name:",
                                    "weight": "Bolder",
                                    "color": "default",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Camera Model:",
                                    "weight": "Bolder",
                                    "color": "default",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Timestamp:",
                                    "weight": "Bolder",
                                    "color": "default",
                                    "spacing": "Small"
                                }
                            ]
                        },
                        {
                            "type": "Column",
                            "width": 65,
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": network_name,
                                    "color": "default"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": camera_name,
                                    "color": "default",
                                    "weight": "Lighter",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": sensor_name,
                                    "color": "default",
                                    "weight": "Lighter",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": model_name,
                                    "weight": "Lighter",
                                    "color": "default",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": timestamp,
                                    "weight": "Lighter",
                                    "color": "default",
                                    "spacing": "Small"
                                }
                            ]
                        }
                    ],
                    "spacing": "Padding",
                    "horizontalAlignment": "Center"
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "Image",
                                    "url": snapshot_link
                                }
                            ]
                        }
                    ],
                    "spacing": "Padding",
                    "horizontalAlignment": "Center"
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "Image",
                                    "altText": "",
                                    "url": "https://developer.webex.com/images/link-icon.png",
                                    "size": "Small",
                                    "width": "30px"
                                }
                            ],
                            "spacing": "Small"
                        },
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": f"[Go to Camera Dashboard Link]({camera_link})",
                                    "horizontalAlignment": "Left",
                                    "size": "Medium"
                                }
                            ],
                            "verticalContentAlignment": "Center",
                            "horizontalAlignment": "Left",
                            "spacing": "Small"
                        }
                    ]
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "Image",
                                    "altText": "",
                                    "url": "https://developer.webex.com/images/link-icon.png",
                                    "size": "Small",
                                    "width": "30px"
                                }
                            ],
                            "spacing": "Small"
                        },
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": f"[Go to Sensor Dashboard Link]({sensor_link})",
                                    "horizontalAlignment": "Left",
                                    "size": "Medium"
                                }
                            ],
                            "verticalContentAlignment": "Center",
                            "horizontalAlignment": "Left",
                            "spacing": "Small"
                        }
                    ]
                }
            ]
        }
    }

    return card
