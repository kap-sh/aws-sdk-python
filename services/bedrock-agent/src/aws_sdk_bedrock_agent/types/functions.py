"""Generated from Smithy shape ``com.amazonaws.bedrockagent#Functions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.function

Functions: TypeAlias = list["aws_sdk_bedrock_agent.types.function.Function"]


# --- restJson1 ser/de ---
def serialize_json(value: Functions) -> list:
    import aws_sdk_bedrock_agent.types.function

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent.types.function.serialize_json(item))
    return out


def deserialize_json(data: list) -> Functions:
    import aws_sdk_bedrock_agent.types.function

    out: Functions = []
    for item in data:
        out.append(aws_sdk_bedrock_agent.types.function.deserialize_json(item))
    return out
