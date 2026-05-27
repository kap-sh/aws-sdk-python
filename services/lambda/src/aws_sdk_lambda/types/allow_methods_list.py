"""Generated from Smithy shape ``com.amazonaws.lambda#AllowMethodsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.method

AllowMethodsList: TypeAlias = list["aws_sdk_lambda.types.method.Method"]


# --- restJson1 ser/de ---
def serialize_json(value: AllowMethodsList) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowMethodsList:
    return list(data)
