"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionResponseTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.function_response_type

FunctionResponseTypeList: TypeAlias = list[
    "aws_sdk_lambda.types.function_response_type.FunctionResponseType"
]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionResponseTypeList) -> list:
    import aws_sdk_lambda.types.function_response_type

    out: list = []
    for item in value:
        out.append(aws_sdk_lambda.types.function_response_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> FunctionResponseTypeList:
    import aws_sdk_lambda.types.function_response_type

    out: FunctionResponseTypeList = []
    for item in data:
        out.append(aws_sdk_lambda.types.function_response_type.deserialize_json(item))
    return out
