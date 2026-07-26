"""Generated from Smithy shape ``com.amazonaws.qbusiness#MessageUsefulness``."""

from typing import Literal, TypeAlias, cast

MessageUsefulness: TypeAlias = Literal[
    "USEFUL",
    "NOT_USEFUL",
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageUsefulness) -> str:
    return value


def deserialize_json(data: str) -> MessageUsefulness:
    return cast(MessageUsefulness, data)
