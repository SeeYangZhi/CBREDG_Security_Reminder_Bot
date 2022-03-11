from telegram import Bot
import os
from decimal import Decimal
import boto3
from botocore.exceptions import ClientError

DYNAMODB = boto3.resource("dynamodb", region_name="ap-southeast-1")


def increment_counter():
    table = DYNAMODB.Table("CBREDG_Security_Alert_Counter")
    try:
        response = table.update_item(
            Key={"index": 0},
            UpdateExpression="set #counter = #counter + :val",
            ExpressionAttributeNames={"#counter": "counter"},
            ExpressionAttributeValues={":val": Decimal(1)},
        )
        if get_counter() > 5:
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


def get_counter():
    table = DYNAMODB.Table("CBREDG_Security_Alert_Counter")
    try:
        response = table.get_item(Key={"index": 0})
    except ClientError as e:
        print(e.response["Error"]["Message"])
    else:
        return response["Item"]["counter"]


TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = "-749393302"
message_list = ["msg0", "msg1", "msg2", "msg3", "msg4", "msg5"]
bot = Bot(token=TOKEN)


def send_message():
    bot.sendMessage(chat_id=CHAT_ID, text=message_list[int(get_counter())])
    increment_counter()


def run(event, context):
    send_message()
