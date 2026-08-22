"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ScopesListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.scope_type

ScopesListType: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.scope_type.ScopeType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScopesListType) -> list:
    return list(value)


def deserialize_json(data: list) -> ScopesListType:
    return [item for item in data if item is not None]
