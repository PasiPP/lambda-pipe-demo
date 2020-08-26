import json
import boto3

def lambda_handler(event, context):
    message = {"foo": "fighters"}
    client = boto3.client('sns')
    response = client.publish(
        TargetArn='arn:aws:sns:us-east-1:821383200340:PasiTopic',
        Message=json.dumps({'default': json.dumps(message)}),
        MessageStructure='json'
    )
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }