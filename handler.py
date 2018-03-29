import json

def main(event, context):
    pathParameters = event.get('pathParameters', {})
    query = event.get('queryStringParameters', {})
    print(json.dumps(event))
    response = {
        'pathParameters': pathParameters,
        'query': query
    }
    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(response)
    }
