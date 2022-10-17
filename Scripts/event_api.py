from azure.storage.blob import BlobServiceClient
import requests
import logging

api_key = ""
conn_string = "DefaultEndpointsProtocol=https;AccountName=autstudentstorage;AccountKey=PM9IioXTd2SWoX/5vHjFIOKkpZTJXX6lyIZkLv5S+n5XIPCOwaU4dGdZalSsOs7TPD59dkz+it4s+AStnNMRBA==;EndpointSuffix=core.windows.net"

# Setting header type for api calls
header = {
    'content-type': 'application/json',
    'api-key': api_key
}

blob_service_client = BlobServiceClient.from_connection_string(conn_string)
container_client = blob_service_client.get_container_client(
    "raspberrypi-videos")

# getting all events
for file in container_client.walk_blobs():
    print(file.name)

    # Post the address information to the correlating event in api
    post_url = "https://api-event-dev.inviol.com/api/v1/events"
    params = {

        {
            "address": [
                {
                    "city": "Auckland",
                    "country": "New Zealand",
                    "name": "Wellesley Street East",
                    "postcode": 1010,
                    "street_number": 55,
                    "suburb": "Auckland City"
                }
            ],
            "confidence": 93.5,
            "device_id": "20d08b4e-c688-4ddb-b307-ec2e74b6a2ad",
            "event_time": "2022-10-10T20:43:56.390Z",
            "latitude": -36.8509,
            "longitude": 174.7645,
            "policy_id": "9b7d0d25-dedd-41f2-b86b-5a08e1dd1d50",
            "type": "edge",
            "videos": [
                {
                    "bbox_video_uri": "",
                    "camera_id": "123e4567-e89b-12d3-a456-426614174001",
                    "event_id": "123e4567-e89b-12d3-a456-426614174000",
                    "original_video_uri": "https://autstudentstorage.blob.core.windows.net/raspberrypi-videos/x 23-09-22 11:44:17.mp4"
                }
            ]
        }
    }
    response = requests.post(post_url, headers=header, json=params)
    print(response)