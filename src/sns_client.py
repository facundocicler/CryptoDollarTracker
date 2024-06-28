import boto3
import logging
import os

logging.basicConfig(level=logging.INFO)

def send_sns_message(message):
    sns = boto3.client('sns', region_name='us-east-2')
    topic_arn = os.getenv('SNS_TOPIC_ARN')
    
    try:
        response = sns.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject='Prueba de mensaje desde AWS SNS'
        )
        return response
    except boto3.exceptions.Boto3Error as e:
        logging.error(f"Error sending SNS message: {e}")
        return None
