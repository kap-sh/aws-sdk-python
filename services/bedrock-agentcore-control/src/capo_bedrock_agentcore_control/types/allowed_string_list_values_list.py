"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AllowedStringListValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.allowed_string_list_value

AllowedStringListValuesList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.allowed_string_list_value.AllowedStringListValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedStringListValuesList) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedStringListValuesList:
    return list(data)
