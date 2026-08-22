"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AllowedStringValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.allowed_string_value

AllowedStringValuesList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.allowed_string_value.AllowedStringValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedStringValuesList) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedStringValuesList:
    return [item for item in data if item is not None]
