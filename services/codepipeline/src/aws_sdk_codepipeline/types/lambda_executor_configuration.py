"""Generated from Smithy shape ``com.amazonaws.codepipeline#LambdaExecutorConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.lambda_function_arn


class LambdaExecutorConfiguration(TypedDict):
    lambda_function_arn: (
        "aws_sdk_codepipeline.types.lambda_function_arn.LambdaFunctionArn"
    )
    """<p>The ARN of the Lambda function used by the action engine.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LambdaExecutorConfiguration) -> dict:
    out: dict = {}
    out["lambdaFunctionArn"] = value["lambda_function_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LambdaExecutorConfiguration:
    out: LambdaExecutorConfiguration = {}  # type: ignore[typeddict-item]
    if "lambdaFunctionArn" in data:
        out["lambda_function_arn"] = data["lambdaFunctionArn"]
    else:
        raise DeserializationError(
            "LambdaExecutorConfiguration.lambda_function_arn required"
        )
    return out
