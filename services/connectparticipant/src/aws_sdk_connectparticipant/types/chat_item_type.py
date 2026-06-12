"""Generated from Smithy shape ``com.amazonaws.connectparticipant#ChatItemType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connectparticipant.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: ChatItemType) -> str:
    return value


def deserialize_json(data: str) -> ChatItemType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChatItemType value: {data!r}")
    return cast(ChatItemType, data)
