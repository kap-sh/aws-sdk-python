"""Generated from Smithy shape ``com.amazonaws.bedrockagent#EnabledMemoryTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.memory_type

EnabledMemoryTypes: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.memory_type.MemoryType"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledMemoryTypes) -> list:
    import aws_sdk_bedrock_agent.types.memory_type

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent.types.memory_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> EnabledMemoryTypes:
    import aws_sdk_bedrock_agent.types.memory_type

    out: EnabledMemoryTypes = []
    for item in data:
        out.append(aws_sdk_bedrock_agent.types.memory_type.deserialize_json(item))
    return out
