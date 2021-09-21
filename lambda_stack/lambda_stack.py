from aws_cdk import (core,
                     aws_apigateway as apigateway,
                     aws_lambda as lambda_)


class LambdaStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str):
        super().__init__(scope, id)

        # API Root
        api = apigateway.RestApi(self, "LambdaApi",
            rest_api_name="Lambda Service",
            description="This service demonstrates deploying a lambda function via cdk.")

        messages = api.root.add_resource("messages")

        # Get All handler
        get_all_handler = lambda_.Function(self, "GetAllMessagesHandler",
            runtime=lambda_.Runtime.NODEJS_14_X,
            code=lambda_.Code.from_asset("lambda_resources"),
            handler="app.lambdaHandler"
        )

        get_messages_integration = apigateway.LambdaIntegration(get_all_handler)
        messages.add_method("GET", get_messages_integration)

