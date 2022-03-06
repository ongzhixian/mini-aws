# CDK CLI

## Install CDK

npm install -g aws-cdk

## Create project

`cdk init app miniAws --language=python`

## Actions to do after you clone 

python -m venv .venv

## Whenever you work

PowerShell
`.\.venv\Scripts\Activate.ps1`

CMD
`.venv\Scripts\activate.bat`

## Actions to do after you pull or start working

pip install -r requirements.txt

## Install constructs

npm install @aws-cdk/aws-lambda
npm install @aws-cdk/aws-apigateway
npm install @aws-cdk/aws-apigatewayv2


## Install for layers

pip install --target=lambda_layers\web\python -r lambda-layers-web-requirements.txt

## CDK

`cdk ls`          list all stacks in the app
`cdk synth`       emits the synthesized CloudFormation template
`cdk deploy`      deploy this stack to your default AWS account/region
`cdk diff`        compare deployed stack with current state


Examples:

cdk bootstrap --profile=mini-aws
cdk deploy --profile=mini-aws
cdk destroy --profile=mini-aws

cdk deploy <StackName>

cdk deploy MiniAwsStack --profile=mini-aws

Add option '--profile=xxx' to use specific profile.


Notes:
    AWS Lambda does not official support ESM.
    As AWS Lambda only supports commonJS, the Lambda entrypoint is a commonJS file.

