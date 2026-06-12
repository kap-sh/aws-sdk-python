"""Generated from Smithy shape ``com.amazonaws.bedrock#ErrorMessages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.error_message

ErrorMessages: TypeAlias = list["aws_sdk_bedrock.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorMessages) -> list:
    return list(value)


def deserialize_json(data: list) -> ErrorMessages:
    return list(data)
