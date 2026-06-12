"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatResponseConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.chat_response_configuration

ChatResponseConfigurations: TypeAlias = list["aws_sdk_qbusiness.types.chat_response_configuration.ChatResponseConfiguration"]


# --- restJson1 ser/de ---
def serialize_json(value: ChatResponseConfigurations) -> list:
    import aws_sdk_qbusiness.types.chat_response_configuration
    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.chat_response_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChatResponseConfigurations:
    import aws_sdk_qbusiness.types.chat_response_configuration
    out: ChatResponseConfigurations = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.chat_response_configuration.deserialize_json(item))
    return out