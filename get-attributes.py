import boto3
import requests
import json

sqs = boto3.client('sqs')
QueueUrl='https://sqs.us-east-1.amazonaws.com/654654587885/myqueue'

response = sqs.get_queue_attributes(
    QueueUrl,
    AttributeNames=[
        'All'
    ]
)

print(response['Attributes']['ApproximateNumberOfMessages'])