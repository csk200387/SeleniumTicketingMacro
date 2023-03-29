import requests
import json


def sendwebhook(url:str, code:str) -> None :
    """Send webhook to discord"""
    headers = { 'Content-Type': 'application/json' }
    data = {
        "embeds": [
            {
                "title": "인편알림",
                "description": f"인증코드 {code} 를 입력해주세요\n유효시간 약 5분",
                "color": 3306509
            }
        ],
        "username": "인편봇"
    }
    requests.post(url, headers=headers, data=json.dumps(data))