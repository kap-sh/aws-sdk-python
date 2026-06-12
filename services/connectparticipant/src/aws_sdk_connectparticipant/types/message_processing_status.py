"""Generated from Smithy shape ``com.amazonaws.connectparticipant#MessageProcessingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connectparticipant.errors import DeserializationError

MessageProcessingStatus: TypeAlias = Literal[
    "PROCESSING",
    "FAILED",
    "REJECTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROCESSING",
        "FAILED",
        "REJECTED",
    )
)


def serialize_json(value: MessageProcessingStatus) -> str:
    return value


def deserialize_json(data: str) -> MessageProcessingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MessageProcessingStatus value: {data!r}")
    return cast(MessageProcessingStatus, data)
