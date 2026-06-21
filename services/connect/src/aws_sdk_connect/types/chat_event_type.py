"""Generated from Smithy shape ``com.amazonaws.connect#ChatEventType``."""

from typing import Literal, TypeAlias, cast

ChatEventType: TypeAlias = Literal[
    "DISCONNECT",
    "MESSAGE",
    "EVENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChatEventType) -> str:
    return value


def deserialize_json(data: str) -> ChatEventType:
    return cast(ChatEventType, data)
