import random

def handler(request):
    number = random.randint(1, 100)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": {
            "random_number": number
        }
    }
