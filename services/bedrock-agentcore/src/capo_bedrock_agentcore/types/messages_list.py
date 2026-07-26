"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MessagesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.message_metadata

MessagesList: TypeAlias = list[
    "capo_bedrock_agentcore.types.message_metadata.MessageMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: MessagesList) -> list:
    import capo_bedrock_agentcore.types.message_metadata

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.message_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> MessagesList:
    import capo_bedrock_agentcore.types.message_metadata

    out: MessagesList = []
    for item in data:
        out.append(capo_bedrock_agentcore.types.message_metadata.deserialize_json(item))
    return out
