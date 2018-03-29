import json

def main(event, context):
    # TODO: check a better way to do this check if is local
    isLocal = 'pathParameters' in event

    # when running local you must use `pathParameters`,
    # but you should use `path` when deployed.
    pathParameters = event.get('pathParameters', event.get('path', {}))

    # when running local you must use `queryStringParameters`,
    # but you should use `query` when deployed.
    query = event.get('queryStringParameters', event.get('query', {}))
    print(json.dumps(event))
    response = {
        'pathParameters': pathParameters,
        'query': query
    }

    if isLocal:
        return {
            'statusCode': 200,
            'headers': {},
            'body': json.dumps(response)
        }
    else:
        return response
