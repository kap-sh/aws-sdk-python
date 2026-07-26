"""Generated from Smithy shape ``com.amazonaws.connect#QueueType``."""

from typing import Literal, TypeAlias, cast

QueueType: TypeAlias = Literal[
    "STANDARD",
    "AGENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueueType) -> str:
    return value


def deserialize_json(data: str) -> QueueType:
    return cast(QueueType, data)
