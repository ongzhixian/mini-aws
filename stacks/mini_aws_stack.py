
from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as aws_lambda,
    aws_apigateway as apigw
    # aws_sqs as sqs,
)
from constructs import Construct

class MiniAwsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "MiniAwsQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        # Defines an AWS Lambda resource
        # my_lambda = _lambda.Function(
        #     self, 'HelloHandler',
        #     function_name="dana_update_handler",
        #     description="hello message handler",
        #     runtime=_lambda.Runtime.PYTHON_3_7,
        #     code=_lambda.Code.from_asset('lambdas'),
        #     handler='hello.handler',
        # )

        # create lambda layers

        web_lib_layer = aws_lambda.LayerVersion(
            self, "web_lib",
            layer_version_name="web_lib",
            code=aws_lambda.Code.from_asset('lambda_layers/web'),
            compatible_runtimes=[aws_lambda.Runtime.PYTHON_3_9],
            description="Packages required for rendering web"
        )

        # create lambdas

        all_lambdas = self.setup_lambdas(web_lib_layer)

        my_lambda = all_lambdas["mini_hello_world"]

        render_page_func = aws_lambda.Function(
            self, "lambda_render_page",
            function_name = "render_page",
            description = "function to render page",
            runtime = aws_lambda.Runtime.PYTHON_3_9,
            code = aws_lambda.Code.from_asset("lambdas"),
            handler = "index.handler",
            layers = [web_lib_layer])

        # setup REST API

        apigw.LambdaRestApi(
            self, id='mini_aws_lambda_rest_api',
            rest_api_name='mini_aws_lambda_rest_api',
            description = "mini-aws REST API endpoint w/Lambda integration",
            handler = all_lambdas["mini_hello_world"],
        )

        api = apigw.RestApi(
            self, "mini_aws_rest_api",
            rest_api_name='mini_aws_rest_api',
            description="mini-aws REST API endpoint"
        )

        get_book_integration = apigw.LambdaIntegration(
            all_lambdas["mini_hello_world"], 
            proxy=False)

        # integration=apigw.HttpIntegration()
        #     url=url,
        #     http_method=str.upper(verb),
        #     proxy=True,
        #     options=aws_apigateway.IntegrationOptions(
        #         request_parameters=method_parameter_set['integration_request_parameters']
        #         if 'integration_request_parameters' in method_parameter_set else None
        #     )
        # )
        

        api.root.add_method("GET", get_book_integration) # GET /

        # GET /test1
        rsrc_test1 = api.root.add_resource("test1")
        rsrc_test1.add_method("GET", apigw.LambdaIntegration(
            all_lambdas["mini_hello_world"]))

        # GET /test2
        rsrc_test2 = api.root.add_resource("test2")
        rsrc_test2.add_method("GET", apigw.LambdaIntegration(
            all_lambdas["mini_some_text_handler"]))

        # GET /test3
        rsrc_test3 = api.root.add_resource("test3")
        rsrc_test3.add_method("GET", apigw.LambdaIntegration(
            all_lambdas["mini_jinja2"]))

        rsrc_test4 = api.root.add_resource("test4")
        rsrc_test4.add_method("GET", apigw.LambdaIntegration(
            all_lambdas["mini_test_static_content"]))

        rsrc_test5 = api.root.add_resource("test5")
        rsrc_test5.add_method("GET", apigw.LambdaIntegration(
            all_lambdas["mini_hello_json"]))

        # items = api.root.add_resource("items")
        # items.add_method("GET", get_book_integration) # GET /items
        # items.add_method("POST") # POST /items

        # item = items.add_resource("{item}")
        # item.add_method("GET", get_book_integration) # GET /items/{item}

        # resource = api.root.add_resource("v1")
        # item = items.add_resource("{item}")
        # item.add_method("GET") # GET /items/{item}
        # resource = api.root.add_resource("v2")


        # Setup deployment

        # deployment = apigw.Deployment(self, "someDeployment", api=api)
        # apigw.Stage(self,"someDef", deployment=deployment, stage_name="$default", )


    def setup_lambdas(self, web_lib_layer):
        result = {}

        result["mini_hello_world"] = aws_lambda.Function(
            self, 'examples_hello_world_handler',
            function_name = "mini_hello_world",
            description = "mini-aws-basic hello world function",
            runtime = aws_lambda.Runtime.PYTHON_3_9,
            code = aws_lambda.Code.from_asset('lambdas'),
            handler = 'examples.hello_world_handler',
        )

        result["mini_hello_json"] = aws_lambda.Function(
            self, 'examples_hello_json_handler',
            function_name = "mini_hello_json",
            description = "mini-aws-basic hello json function",
            runtime = aws_lambda.Runtime.PYTHON_3_9,
            code = aws_lambda.Code.from_asset('lambdas'),
            handler = 'examples.hello_json_handler',
        )

        #some_text_handler
        result["mini_some_text_handler"] = aws_lambda.Function(
            self, 'examples_mini_some_text_handler',
            function_name = "mini_some_text_handler",
            description = "mini-aws-basic some text function",
            runtime = aws_lambda.Runtime.PYTHON_3_9,
            code = aws_lambda.Code.from_asset('lambdas'),
            handler = 'examples.some_text_handler',
        )

        result["mini_jinja2"] = aws_lambda.Function(
            self, 'web_lambda_handler',
            function_name = "mini_jinja2",
            description = "mini-aws test jinja2",
            runtime = aws_lambda.Runtime.PYTHON_3_9,
            code = aws_lambda.Code.from_asset('lambdas'),
            handler = 'web.lambda_handler',
            layers=[web_lib_layer]
        )

        result["mini_test_static_content"] = aws_lambda.Function(
            self, 'web_example_static_content_handler',
            function_name = "mini_test_static_content",
            description = "mini-aws-test service static content",
            runtime = aws_lambda.Runtime.PYTHON_3_9,
            code = aws_lambda.Code.from_asset('lambdas'),
            handler = 'web.example_static_content_handler',
            layers=[web_lib_layer]
        )

        return result