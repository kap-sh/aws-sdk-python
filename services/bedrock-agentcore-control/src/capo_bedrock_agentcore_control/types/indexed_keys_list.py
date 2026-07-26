"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#IndexedKeysList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.indexed_key

IndexedKeysList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.indexed_key.IndexedKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: IndexedKeysList) -> list:
    import capo_bedrock_agentcore_control.types.indexed_key

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.indexed_key.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IndexedKeysList:
    import capo_bedrock_agentcore_control.types.indexed_key

    out: IndexedKeysList = []
    for item in data:
        out.append(
            capo_bedrock_agentcore_control.types.indexed_key.deserialize_json(item)
        )
    return out
