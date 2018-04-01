import json

def local(event, context):
    # Using AWS Sam Local, the input event and the return output are different.
    # This function modifies event and pass it to main handler
    event['path'] = event.get('pathParameters', {})
    event['query'] = event.get('queryStringParameters', {})
    body = main(event, context)
    # must include one of: body, headers or statusCode in the response object
    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(body)
    }

def main(event, context):
    path = event.get('path', {})
    query = event.get('query', {})
    return {
        'path': path,
        'query': query
    }
