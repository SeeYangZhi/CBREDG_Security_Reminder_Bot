import boto3
import os
import json
from telegram import Bot
from decimal import Decimal
from botocore.exceptions import ClientError

DYNAMODB = boto3.resource("dynamodb", region_name="ap-southeast-1")
TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
bot = Bot(token=TOKEN)


def increment_counter():
    table = DYNAMODB.Table("CBREDG_Weekly_Security_Message")
    try:
        response = table.update_item(
            Key={"index": 0},
            UpdateExpression="set #counter = #counter + :val",
            ExpressionAttributeNames={"#counter": "counter"},
            ExpressionAttributeValues={":val": Decimal(1)},
        )
        if get_counter() > len(get_messages()) - 1:
            table.update_item(
                Key={"index": 0},
                UpdateExpression="set #counter = :val",
                ExpressionAttributeNames={"#counter": "counter"},
                ExpressionAttributeValues={":val": Decimal(0)},
            )
    except ClientError as e:
        print(e.response["Error"]["Message"])
    else:
        return response


def get_messages():
    f = open("messages.json")
    messages = json.loads(f.read())
    f.close()
    messages_list = []
    for category in messages:
        for message in messages[category]:
            messages_list.append(message)
    return messages_list


def get_counter():
    table = DYNAMODB.Table("CBREDG_Weekly_Security_Message")
    try:
        response = table.get_item(Key={"index": 0})
    except ClientError as e:
        print(e.response["Error"]["Message"])
    else:
        return int(response["Item"]["counter"])


def send_message():
    message_list = get_messages()
    bot.sendMessage(
        chat_id=CHAT_ID, text=message_list[get_counter()], parse_mode="HTML"
    )
    increment_counter()


def run(event, context):
    send_message()
