"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsLambdaFunctionLayerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_lambda_function_layer

AwsLambdaFunctionLayerList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_lambda_function_layer.AwsLambdaFunctionLayer"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsLambdaFunctionLayerList) -> list:
    import aws_sdk_securityhub.types.aws_lambda_function_layer

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_lambda_function_layer.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsLambdaFunctionLayerList:
    import aws_sdk_securityhub.types.aws_lambda_function_layer

    out: AwsLambdaFunctionLayerList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_lambda_function_layer.deserialize_json(item)
        )
    return out
