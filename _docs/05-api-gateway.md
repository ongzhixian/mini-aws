# Notes on AWS API Gateway

MockIntegration - can be used to test APIs. This is the default integration if one is not specified.

LambdaIntegration - can be used to invoke an AWS Lambda function.

AwsIntegration - can be used to invoke arbitrary AWS service APIs.

HttpIntegration - can be used to invoke HTTP endpoints.



HTTP integration URIs

You can use a stage variable as part of an HTTP integration URI, as shown in the following examples.

A full URI without protocol – http://${stageVariables.<variable_name>}
A full domain               – http://${stageVariables.<variable_name>}/resource/operation
A subdomain                 – http://${stageVariables.<variable_name>}.example.com/resource/operation
A path                      – http://example.com/${stageVariables.<variable_name>}/bar
A query string              – http://example.com/foo?q=${stageVariables.<variable_name>}

https://api-id.execute-api.region.amazonaws.com/stage


Output format of a Lambda function for proxy integration
In Lambda proxy integration, API Gateway requires the backend Lambda function to return output according to the following JSON format:

{
    "isBase64Encoded": true|false,
    "statusCode": httpStatusCode,
    "headers": { "headerName": "headerValue", ... },
    "multiValueHeaders": { "headerName": ["headerValue", "headerValue2", ...], ... },
    "body": "..."
}



# Reference

https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-basic-concept.html

https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html