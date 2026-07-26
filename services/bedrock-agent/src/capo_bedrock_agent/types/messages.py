"""Generated from Smithy shape ``com.amazonaws.bedrockagent#Messages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.message

Messages: TypeAlias = list["capo_bedrock_agent.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: Messages) -> list:
    import capo_bedrock_agent.types.message

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.message.serialize_json(item))
    return out


def deserialize_json(data: list) -> Messages:
    import capo_bedrock_agent.types.message

    out: Messages = []
    for item in data:
        out.append(capo_bedrock_agent.types.message.deserialize_json(item))
    return out
