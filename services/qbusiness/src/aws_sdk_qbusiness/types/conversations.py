"""Generated from Smithy shape ``com.amazonaws.qbusiness#Conversations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.conversation

Conversations: TypeAlias = list["aws_sdk_qbusiness.types.conversation.Conversation"]


# --- restJson1 ser/de ---
def serialize_json(value: Conversations) -> list:
    import aws_sdk_qbusiness.types.conversation

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.conversation.serialize_json(item))
    return out


def deserialize_json(data: list) -> Conversations:
    import aws_sdk_qbusiness.types.conversation

    out: Conversations = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.conversation.deserialize_json(item))
    return out
