"""Generated from Smithy shape ``com.amazonaws.connectparticipant#ChatItemType``."""

from typing import Literal, TypeAlias, cast

ChatItemType: TypeAlias = Literal[
    "TYPING",
    "PARTICIPANT_JOINED",
    "PARTICIPANT_LEFT",
    "CHAT_ENDED",
    "TRANSFER_SUCCEEDED",
    "TRANSFER_FAILED",
    "MESSAGE",
    "EVENT",
    "ATTACHMENT",
    "CONNECTION_ACK",
    "MESSAGE_DELIVERED",
    "MESSAGE_READ",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChatItemType) -> str:
    return value


def deserialize_json(data: str) -> ChatItemType:
    return cast(ChatItemType, data)
