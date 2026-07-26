"""Generated from Smithy shape ``com.amazonaws.qbusiness#Conversations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.conversation

Conversations: TypeAlias = list["capo_qbusiness.types.conversation.Conversation"]


# --- restJson1 ser/de ---
def serialize_json(value: Conversations) -> list:
    import capo_qbusiness.types.conversation

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.conversation.serialize_json(item))
    return out


def deserialize_json(data: list) -> Conversations:
    import capo_qbusiness.types.conversation

    out: Conversations = []
    for item in data:
        out.append(capo_qbusiness.types.conversation.deserialize_json(item))
    return out
