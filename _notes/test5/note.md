# Test notes

Notes on writing Lambda functions suitable for API Gateway's Lambda integration.

```python: Stack
    api = apigw.RestApi(
        self, "mini_aws_rest_api",
        rest_api_name='mini_aws_rest_api',
        description="mini-aws REST API endpoint"
    )

    # Adding proxied Lambda integrations like so
    # GET /test1
    rsrc_test1 = api.root.add_resource("test1")
    rsrc_test1.add_method("GET", apigw.LambdaIntegration(all_lambdas["mini_hello_world"]))
```

```python: Working lambda
def hello_world_handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello, CDK! You have hit {}\n'.format(event['path'])
    }
```

Execution log for request 41fc2a48-605e-4df7-99b9-43456c10fe95
Sat Mar 05 15:47:32 UTC 2022 : Starting execution for request: 41fc2a48-605e-4df7-99b9-43456c10fe95
Sat Mar 05 15:47:32 UTC 2022 : HTTP Method: GET, Resource Path: /test1
Sat Mar 05 15:47:32 UTC 2022 : Method request path: {}
Sat Mar 05 15:47:32 UTC 2022 : Method request query string: {}
Sat Mar 05 15:47:32 UTC 2022 : Method request headers: {}
Sat Mar 05 15:47:32 UTC 2022 : Method request body before transformations: 
Sat Mar 05 15:47:32 UTC 2022 : Endpoint request URI: https://lambda.us-east-1.amazonaws.com/2015-03-31/functions/arn:aws:lambda:us-east-1:009167579319:function:mini_hello_world/invocations
Sat Mar 05 15:47:32 UTC 2022 : Endpoint request headers: {X-Amz-Date=20220305T154732Z, x-amzn-apigateway-api-id=8a1b7vlz9f, Accept=application/json, 
                                User-Agent=AmazonAPIGateway_8a1b7vlz9f, Host=lambda.us-east-1.amazonaws.com, X-Amz-Content-Sha256=93d70612a3944ea9b2a72e61c9df186e75b7623c9abcd1e083864a54e838e942, 
                                X-Amzn-Trace-Id=Root=1-62238614-3a988ffa3677d72435c58744, x-amzn-lambda-integration-tag=41fc2a48-605e-4df7-99b9-43456c10fe95, 
                                Authorization=*********************************************************************************************************************************************************************************************************************************************************************************************************************************************358b99, 
                                X-Amz-Source-Arn=arn:aws:execute-api:us-east-1:009167579319:8a1b7vlz9f/test-invoke-stage/GET/test1, 
                                X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLWVhc3QtMSJGMEQCICFPa9LBwXMlMxlr0+0LmuCMB3MPOUViCOvozsQjnfGIAiA1cteVrxxRY+/Z9d/N8owiO4Ujk2yn7mHBHQNH7+TWoCr6Awh4EAAa [TRUNCATED]
Sat Mar 05 15:47:32 UTC 2022 : Endpoint request body after transformations: {
                                "resource":"/test1","path":"/test1","httpMethod":"GET","headers":null,"multiValueHeaders":null,
                                "queryStringParameters":null,"multiValueQueryStringParameters":null,"pathParameters":null,"stageVariables":null,
                                "requestContext":{"resourceId":"ya35h0","resourcePath":"/test1","httpMethod":"GET","extendedRequestId":"OhHjPFP9oAMFkpg=",
                                "requestTime":"05/Mar/2022:15:47:32 +0000","path":"/test1","accountId":"009167579319","protocol":"HTTP/1.1","stage":"test-invoke-stage",
                                "domainPrefix":"testPrefix","requestTimeEpoch":1646495252562,"requestId":"41fc2a48-605e-4df7-99b9-43456c10fe95",
                                "identity":{"cognitoIdentityPoolId":null,"cognitoIdentityId":null,"apiKey":"test-invoke-api-key","principalOrgId":null,"cognitoAuthenticationType":null,"userArn":"arn:aws:iam::009167579319:user/zhixian","apiKeyId":"test-invoke-api-key-id","userAgent":"aws-internal/3 aws-sdk-java/1.12.159 Linux/5.4.172-100.336.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/25.322-b06 java/1.8.0_322 vendor/Oracle_Corporati [TRUNCATED]
Sat Mar 05 15:47:32 UTC 2022 : Sending request to https://lambda.us-east-1.amazonaws.com/2015-03-31/functions/arn:aws:lambda:us-east-1:009167579319:function:mini_hello_world/invocations
Sat Mar 05 15:47:32 UTC 2022 : Received response. Status: 200, Integration latency: 241 ms
Sat Mar 05 15:47:32 UTC 2022 : Endpoint response headers: {Date=Sat, 05 Mar 2022 15:47:32 GMT, Content-Type=application/json, Content-Length=107, Connection=keep-alive, x-amzn-RequestId=144f1a8c-1d4d-4044-91cf-7539c3bf6ba4, x-amzn-Remapped-Content-Length=0, X-Amz-Executed-Version=$LATEST, X-Amzn-Trace-Id=root=1-62238614-3a988ffa3677d72435c58744;sampled=0}
Sat Mar 05 15:47:32 UTC 2022 : Endpoint response body before transformations: {"statusCode": 200, "headers": {"Content-Type": "text/plain"}, "body": "Hello, CDK! You have hit /test1\n"}
Sat Mar 05 15:47:32 UTC 2022 : Method response body after transformations: Hello, CDK! You have hit /test1
Sat Mar 05 15:47:32 UTC 2022 : Method response headers: {Content-Type=text/plain, X-Amzn-Trace-Id=Root=1-62238614-3a988ffa3677d72435c58744;Sampled=0}
Sat Mar 05 15:47:32 UTC 2022 : Successfully completed execution
Sat Mar 05 15:47:32 UTC 2022 : Method completed with status: 200



```python: No work
def some_text_handler(event, context):
    return "hello from some_text_handler"
```

Execution log for request ebc6434a-2151-4cfa-8889-38dffec3eced
Sat Mar 05 15:39:57 UTC 2022 : Starting execution for request: ebc6434a-2151-4cfa-8889-38dffec3eced
Sat Mar 05 15:39:57 UTC 2022 : HTTP Method: GET, Resource Path: /test2
Sat Mar 05 15:39:57 UTC 2022 : Method request path: {}
Sat Mar 05 15:39:57 UTC 2022 : Method request query string: {}
Sat Mar 05 15:39:57 UTC 2022 : Method request headers: {}
Sat Mar 05 15:39:57 UTC 2022 : Method request body before transformations: 
Sat Mar 05 15:39:57 UTC 2022 : Endpoint request URI: https://lambda.us-east-1.amazonaws.com/2015-03-31/functions/arn:aws:lambda:us-east-1:009167579319:function:mini_some_text_handler/invocations
Sat Mar 05 15:39:57 UTC 2022 : Endpoint request headers: {X-Amz-Date=20220305T153957Z, x-amzn-apigateway-api-id=8a1b7vlz9f, Accept=application/json, User-Agent=AmazonAPIGateway_8a1b7vlz9f, Host=lambda.us-east-1.amazonaws.com, X-Amz-Content-Sha256=63acc0155b8bfc57c8de0aeee024adc864b393af8f08c908f9b4771c6ba358bd, X-Amzn-Trace-Id=Root=1-6223844d-43b44adc91e919328a918469, x-amzn-lambda-integration-tag=ebc6434a-2151-4cfa-8889-38dffec3eced, Authorization=*********************************************************************************************************************************************************************************************************************************************************************************************************************************************e4b2ca, X-Amz-Source-Arn=arn:aws:execute-api:us-east-1:009167579319:8a1b7vlz9f/test-invoke-stage/GET/test2, X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLWVhc3QtMSJGMEQCIFPAjwNHLZr4BkBd6/tKFzg1UhRmxyYbQNQxI2bXd+4MAiBIQ5fIhlE+XT4JN31ALjJnSjBmvoW94VdJttH4YOb2JSr6Awh3EAAa [TRUNCATED]
Sat Mar 05 15:39:57 UTC 2022 : Endpoint request body after transformations: {"resource":"/test2","path":"/test2","httpMethod":"GET","headers":null,"multiValueHeaders":null,"queryStringParameters":null,"multiValueQueryStringParameters":null,"pathParameters":null,"stageVariables":null,"requestContext":{"resourceId":"2p45uf","resourcePath":"/test2","httpMethod":"GET","extendedRequestId":"OhGcMGaQIAMF9yw=","requestTime":"05/Mar/2022:15:39:57 +0000","path":"/test2","accountId":"009167579319","protocol":"HTTP/1.1","stage":"test-invoke-stage","domainPrefix":"testPrefix","requestTimeEpoch":1646494797853,"requestId":"ebc6434a-2151-4cfa-8889-38dffec3eced","identity":{"cognitoIdentityPoolId":null,"cognitoIdentityId":null,"apiKey":"test-invoke-api-key","principalOrgId":null,"cognitoAuthenticationType":null,"userArn":"arn:aws:iam::009167579319:user/zhixian","apiKeyId":"test-invoke-api-key-id","userAgent":"aws-internal/3 aws-sdk-java/1.12.159 Linux/5.4.172-100.336.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/25.322-b06 java/1.8.0_322 vendor/Oracle_Corporati [TRUNCATED]
Sat Mar 05 15:39:57 UTC 2022 : Sending request to https://lambda.us-east-1.amazonaws.com/2015-03-31/functions/arn:aws:lambda:us-east-1:009167579319:function:mini_some_text_handler/invocations
Sat Mar 05 15:39:58 UTC 2022 : Received response. Status: 200, Integration latency: 227 ms
Sat Mar 05 15:39:58 UTC 2022 : Endpoint response headers: {Date=Sat, 05 Mar 2022 15:39:58 GMT, Content-Type=application/json, Content-Length=30, Connection=keep-alive, x-amzn-RequestId=2b3efc48-81f2-4543-8289-7584ebf63a51, x-amzn-Remapped-Content-Length=0, X-Amz-Executed-Version=$LATEST, X-Amzn-Trace-Id=root=1-6223844d-43b44adc91e919328a918469;sampled=0}
Sat Mar 05 15:39:58 UTC 2022 : Endpoint response body before transformations: "hello from some_text_handler"
Sat Mar 05 15:39:58 UTC 2022 : Execution failed due to configuration error: Malformed Lambda proxy response
Sat Mar 05 15:39:58 UTC 2022 : Method completed with status: 502


```python:no work
def example_static_content_handler(event, context):
    html = '<html><head><title>HTML from API Gateway/Lambda</title></head><body><h1>HTML from API Gateway/Lambda</h1></body></html>'
    context.succeed(html)
```
Execution log for request b50a12c6-d619-4147-b2a2-bb5d42586463
Sat Mar 05 15:50:39 UTC 2022 : Starting execution for request: b50a12c6-d619-4147-b2a2-bb5d42586463
Sat Mar 05 15:50:39 UTC 2022 : HTTP Method: GET, Resource Path: /test4
Sat Mar 05 15:50:39 UTC 2022 : Method request path: {}
Sat Mar 05 15:50:39 UTC 2022 : Method request query string: {}
Sat Mar 05 15:50:39 UTC 2022 : Method request headers: {}
Sat Mar 05 15:50:39 UTC 2022 : Method request body before transformations: 
Sat Mar 05 15:50:39 UTC 2022 : Endpoint request URI: https://lambda.us-east-1.amazonaws.com/2015-03-31/functions/arn:aws:lambda:us-east-1:009167579319:function:mini_test_static_content/invocations
Sat Mar 05 15:50:39 UTC 2022 : Endpoint request headers: {X-Amz-Date=20220305T155039Z, x-amzn-apigateway-api-id=8a1b7vlz9f, Accept=application/json, User-Agent=AmazonAPIGateway_8a1b7vlz9f, Host=lambda.us-east-1.amazonaws.com, X-Amz-Content-Sha256=9cc4896a8d83f4409d850229c364946834fba1c6d8675734fdb00323928af31a, X-Amzn-Trace-Id=Root=1-622386cf-fadd572d491d1b05e6f7433a, x-amzn-lambda-integration-tag=b50a12c6-d619-4147-b2a2-bb5d42586463, Authorization=*********************************************************************************************************************************************************************************************************************************************************************************************************************************************248d7f, X-Amz-Source-Arn=arn:aws:execute-api:us-east-1:009167579319:8a1b7vlz9f/test-invoke-stage/GET/test4, X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLWVhc3QtMSJHMEUCIGm391LbO9Lef9YUxBbYRUiRNLq+zvCYidvOzln4IB9aAiEAygrP6P9K5jxIszsBiYV2mGsB588I40/jEAOysq+PFQoq+gMIeBAA [TRUNCATED]
Sat Mar 05 15:50:39 UTC 2022 : Endpoint request body after transformations: {"resource":"/test4","path":"/test4","httpMethod":"GET","headers":null,"multiValueHeaders":null,"queryStringParameters":null,"multiValueQueryStringParameters":null,"pathParameters":null,"stageVariables":null,"requestContext":{"resourceId":"qs9bus","resourcePath":"/test4","httpMethod":"GET","extendedRequestId":"OhIAbGGIIAMFaAQ=","requestTime":"05/Mar/2022:15:50:39 +0000","path":"/test4","accountId":"009167579319","protocol":"HTTP/1.1","stage":"test-invoke-stage","domainPrefix":"testPrefix","requestTimeEpoch":1646495439366,"requestId":"b50a12c6-d619-4147-b2a2-bb5d42586463","identity":{"cognitoIdentityPoolId":null,"cognitoIdentityId":null,"apiKey":"test-invoke-api-key","principalOrgId":null,"cognitoAuthenticationType":null,"userArn":"arn:aws:iam::009167579319:user/zhixian","apiKeyId":"test-invoke-api-key-id","userAgent":"aws-internal/3 aws-sdk-java/1.12.159 Linux/5.4.172-100.336.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/25.322-b06 java/1.8.0_322 vendor/Oracle_Corporati [TRUNCATED]
Sat Mar 05 15:50:39 UTC 2022 : Sending request to https://lambda.us-east-1.amazonaws.com/2015-03-31/functions/arn:aws:lambda:us-east-1:009167579319:function:mini_test_static_content/invocations
Sat Mar 05 15:50:39 UTC 2022 : Received response. Status: 200, Integration latency: 433 ms
Sat Mar 05 15:50:39 UTC 2022 : Endpoint response headers: {Date=Sat, 05 Mar 2022 15:50:39 GMT, Content-Type=application/json, Content-Length=273, Connection=keep-alive, x-amzn-RequestId=c2fdeda4-0849-4da2-bc61-36a9ed8b698d, X-Amz-Function-Error=Unhandled, x-amzn-Remapped-Content-Length=0, X-Amz-Executed-Version=$LATEST, X-Amzn-Trace-Id=root=1-622386cf-fadd572d491d1b05e6f7433a;sampled=0}
Sat Mar 05 15:50:39 UTC 2022 : Endpoint response body before transformations: {"errorMessage": "'LambdaContext' object has no attribute 'succeed'", "errorType": "AttributeError", "requestId": "c2fdeda4-0849-4da2-bc61-36a9ed8b698d", "stackTrace": ["  File \"/var/task/web.py\", line 18, in example_static_content_handler\n    context.succeed(html)\n"]}
Sat Mar 05 15:50:39 UTC 2022 : Lambda execution failed with status 200 due to customer function error: 'LambdaContext' object has no attribute 'succeed'. Lambda request id: c2fdeda4-0849-4da2-bc61-36a9ed8b698d
Sat Mar 05 15:50:39 UTC 2022 : Method completed with status: 502