"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#Messages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.message

Messages: TypeAlias = list["aws_sdk_bedrock_runtime.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: Messages) -> list:
    import aws_sdk_bedrock_runtime.types.message

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_runtime.types.message.serialize_json(item))
    return out


def deserialize_json(data: list) -> Messages:
    import aws_sdk_bedrock_runtime.types.message

    out: Messages = []
    for item in data:
        out.append(aws_sdk_bedrock_runtime.types.message.deserialize_json(item))
    return out
