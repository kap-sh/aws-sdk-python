"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyStatusReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.string

PolicyStatusReasons: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyStatusReasons) -> list:
    return list(value)


def deserialize_json(data: list) -> PolicyStatusReasons:
    return list(data)
