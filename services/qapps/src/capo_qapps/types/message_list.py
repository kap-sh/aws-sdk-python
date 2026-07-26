"""Generated from Smithy shape ``com.amazonaws.qapps#MessageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qapps.types.conversation_message

MessageList: TypeAlias = list[
    "capo_qapps.types.conversation_message.ConversationMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageList) -> list:
    import capo_qapps.types.conversation_message

    out: list = []
    for item in value:
        out.append(capo_qapps.types.conversation_message.serialize_json(item))
    return out


def deserialize_json(data: list) -> MessageList:
    import capo_qapps.types.conversation_message

    out: MessageList = []
    for item in data:
        out.append(capo_qapps.types.conversation_message.deserialize_json(item))
    return out
