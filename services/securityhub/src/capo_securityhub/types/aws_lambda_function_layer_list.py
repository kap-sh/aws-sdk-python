"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsLambdaFunctionLayerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_lambda_function_layer

AwsLambdaFunctionLayerList: TypeAlias = list[
    "capo_securityhub.types.aws_lambda_function_layer.AwsLambdaFunctionLayer"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsLambdaFunctionLayerList) -> list:
    import capo_securityhub.types.aws_lambda_function_layer

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_lambda_function_layer.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsLambdaFunctionLayerList:
    import capo_securityhub.types.aws_lambda_function_layer

    out: AwsLambdaFunctionLayerList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_lambda_function_layer.deserialize_json(item)
        )
    return out
