"""Generated from Smithy shape ``com.amazonaws.mediatailor#MessageType``."""

from typing import Literal, TypeAlias, cast

MessageType: TypeAlias = Literal[
    "SPLICE_INSERT",
    "TIME_SIGNAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageType) -> str:
    return value


def deserialize_json(data: str) -> MessageType:
    return cast(MessageType, data)
