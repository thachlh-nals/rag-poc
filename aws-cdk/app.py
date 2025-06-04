#!/usr/bin/env python3
import aws_cdk as cdk
from cdk_stack import S3CloudFrontStack

app = cdk.App()
S3CloudFrontStack(app, "S3CloudFrontStack")

app.synth()

