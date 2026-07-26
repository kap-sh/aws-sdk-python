"""Generated from Smithy shape ``com.amazonaws.pinpoint#MessageType``."""

from typing import Literal, TypeAlias, cast

MessageType: TypeAlias = Literal[
    "TRANSACTIONAL",
    "PROMOTIONAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageType) -> str:
    return value


def deserialize_json(data: str) -> MessageType:
    return cast(MessageType, data)
