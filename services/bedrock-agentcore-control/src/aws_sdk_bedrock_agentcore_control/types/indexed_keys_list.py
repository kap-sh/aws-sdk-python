"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#IndexedKeysList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.indexed_key

IndexedKeysList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.indexed_key.IndexedKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: IndexedKeysList) -> list:
    import aws_sdk_bedrock_agentcore_control.types.indexed_key

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.indexed_key.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IndexedKeysList:
    import aws_sdk_bedrock_agentcore_control.types.indexed_key

    out: IndexedKeysList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.indexed_key.deserialize_json(item)
        )
    return out
