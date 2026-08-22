"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyStatusReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.string

PolicyStatusReasons: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyStatusReasons) -> list:
    return list(value)


def deserialize_json(data: list) -> PolicyStatusReasons:
    return [item for item in data if item is not None]
