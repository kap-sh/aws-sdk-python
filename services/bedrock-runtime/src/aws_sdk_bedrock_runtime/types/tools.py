"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#Tools``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.tool

Tools: TypeAlias = list["aws_sdk_bedrock_runtime.types.tool.Tool"]


# --- restJson1 ser/de ---
def serialize_json(value: Tools) -> list:
    import aws_sdk_bedrock_runtime.types.tool

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_runtime.types.tool.serialize_json(item))
    return out


def deserialize_json(data: list) -> Tools:
    import aws_sdk_bedrock_runtime.types.tool

    out: Tools = []
    for item in data:
        out.append(aws_sdk_bedrock_runtime.types.tool.deserialize_json(item))
    return out
