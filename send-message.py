import boto3
import requests
import json

sqs = boto3.client('sqs')

id = requests.get('https://ids.pods.uvarc.io')

response = sqs.send_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/654654587885/myqueue',
    MessageBody=id.text,
    MessageAttributes={
        'Project': {
            'StringValue': 'Project X',
            'DataType': 'String'
        },
         'Flavor': {
            'StringValue': 'Vanilla',
            'DataType': 'String'
        }
    }
)

print(response)

