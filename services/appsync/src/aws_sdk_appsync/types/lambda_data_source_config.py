"""Generated from Smithy shape ``com.amazonaws.appsync#LambdaDataSourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.string


class LambdaDataSourceConfig(TypedDict, closed=True):
    lambda_function_arn: "aws_sdk_appsync.types.string.String"
    """<p>The Amazon Resource Name (ARN) for the Lambda function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaDataSourceConfig) -> dict:
    out: dict = {}
    out["lambdaFunctionArn"] = value["lambda_function_arn"]
    return out


def deserialize_json(data: dict) -> LambdaDataSourceConfig:
    out: LambdaDataSourceConfig = {}  # type: ignore[typeddict-item]
    if "lambdaFunctionArn" in data:
        out["lambda_function_arn"] = data["lambdaFunctionArn"]
    else:
        raise DeserializationError(
            "LambdaDataSourceConfig.lambda_function_arn required"
        )
    return out
