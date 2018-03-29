# aws-lambda-python-api-example
Basic example code for running Python API on AWS Lambda, deploying with Serverless and running local with AWS Sam Local.

# Requirements

- Python 3.6
- Docker
- **AWS Sam Local**: https://github.com/awslabs/aws-sam-local
- Serverless

# Run Local API:

```
sam local start-api
```
Request: http://localhost:3000/api/hello/world?looks=good
