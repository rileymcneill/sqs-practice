import boto3
import requests
import json

sqs = boto3.client('sqs')
QueueUrl='https://sqs.us-east-1.amazonaws.com/654654587885/myqueue'

def delete_msg(handle):
    delete = sqs.delete_message(
        QueueUrl=QueueUrl,
        ReceiptHandle=response['Messages'][0]['ReceiptHandle']
    )

response = sqs.receive_message(
    QueueUrl=QueueUrl,
    AttributeNames=[
        'All'
    ]
)

print(response)
print(response['Messages'][0]['Body'])
delete_msg(handle)
