"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Memories``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.memory

Memories: TypeAlias = list["aws_sdk_bedrock_agent_runtime.types.memory.Memory"]


# --- restJson1 ser/de ---
def serialize_json(value: Memories) -> list:
    import aws_sdk_bedrock_agent_runtime.types.memory

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent_runtime.types.memory.serialize_json(item))
    return out


def deserialize_json(data: list) -> Memories:
    import aws_sdk_bedrock_agent_runtime.types.memory

    out: Memories = []
    for item in data:
        out.append(aws_sdk_bedrock_agent_runtime.types.memory.deserialize_json(item))
    return out
