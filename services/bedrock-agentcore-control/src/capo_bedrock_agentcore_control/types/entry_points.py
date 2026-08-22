"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EntryPoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.entry_point

EntryPoints: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.entry_point.entryPoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: EntryPoints) -> list:
    return list(value)


def deserialize_json(data: list) -> EntryPoints:
    return [item for item in data if item is not None]
