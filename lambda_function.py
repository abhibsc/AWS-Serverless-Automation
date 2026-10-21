import boto3
import os

ec2 = boto3.client("ec2")


def lambda_handler(event, context):
    instance_id = os.environ["INSTANCE_ID"]
    action = event.get("action", "start").lower()

    if action == "start":
        ec2.start_instances(InstanceIds=[instance_id])
        message = f"Start request sent for {instance_id}"

    elif action == "stop":
        ec2.stop_instances(InstanceIds=[instance_id])
        message = f"Stop request sent for {instance_id}"

    else:
        raise ValueError("Action must be start or stop")

    print(message)

    return {
        "statusCode": 200,
        "body": message
    }