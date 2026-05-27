"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.function_configuration

FunctionList: TypeAlias = list[
    "aws_sdk_lambda.types.function_configuration.FunctionConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionList) -> list:
    import aws_sdk_lambda.types.function_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_lambda.types.function_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> FunctionList:
    import aws_sdk_lambda.types.function_configuration

    out: FunctionList = []
    for item in data:
        out.append(aws_sdk_lambda.types.function_configuration.deserialize_json(item))
    return out
