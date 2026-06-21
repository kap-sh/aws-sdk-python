"""Generated from Smithy shape ``com.amazonaws.qbusiness#MessageType``."""

from typing import Literal, TypeAlias, cast

MessageType: TypeAlias = Literal[
    "USER",
    "SYSTEM",
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageType) -> str:
    return value


def deserialize_json(data: str) -> MessageType:
    return cast(MessageType, data)
