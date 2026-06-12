"""Generated from Smithy shape ``com.amazonaws.connect#FunctionArnsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.function_arn

FunctionArnsList: TypeAlias = list["aws_sdk_connect.types.function_arn.FunctionArn"]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionArnsList) -> list:
    return list(value)


def deserialize_json(data: list) -> FunctionArnsList:
    return list(data)
