"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Parameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.parameter

Parameters: TypeAlias = list["aws_sdk_bedrock_agent_runtime.types.parameter.Parameter"]


# --- restJson1 ser/de ---
def serialize_json(value: Parameters) -> list:
    import aws_sdk_bedrock_agent_runtime.types.parameter

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent_runtime.types.parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> Parameters:
    import aws_sdk_bedrock_agent_runtime.types.parameter

    out: Parameters = []
    for item in data:
        out.append(aws_sdk_bedrock_agent_runtime.types.parameter.deserialize_json(item))
    return out
