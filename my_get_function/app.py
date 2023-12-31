import os
import json
from db_info import DBInfo
# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e
    dbinfo = DBInfo()

    res = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",  # ここを適切なオリジンに設定
            "Access-Control-Allow-Methods": "GET,OPTIONS",  # 許可するメソッドを設定
            "Access-Control-Allow-Headers": "Content-Type"  # 許可するヘッダーを設定
        },
        "body": json.dumps({
            "message": "get api(host:{}/port:{}/)".format(dbinfo.connections['host'], dbinfo.connections['port']),
            "UserName": os.environ.get('UserName', "UserNameError"),
            "UserType": os.environ.get('UserType', 9999),
            # "location": ip.text.replace("\n", "")
        }),
    }
    return res
