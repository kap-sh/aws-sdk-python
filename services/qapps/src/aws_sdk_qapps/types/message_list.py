"""Generated from Smithy shape ``com.amazonaws.qapps#MessageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qapps.types.conversation_message

MessageList: TypeAlias = list[
    "aws_sdk_qapps.types.conversation_message.ConversationMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageList) -> list:
    import aws_sdk_qapps.types.conversation_message

    out: list = []
    for item in value:
        out.append(aws_sdk_qapps.types.conversation_message.serialize_json(item))
    return out


def deserialize_json(data: list) -> MessageList:
    import aws_sdk_qapps.types.conversation_message

    out: MessageList = []
    for item in data:
        out.append(aws_sdk_qapps.types.conversation_message.deserialize_json(item))
    return out
