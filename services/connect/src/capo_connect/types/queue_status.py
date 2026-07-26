"""Generated from Smithy shape ``com.amazonaws.connect#QueueStatus``."""

from typing import Literal, TypeAlias, cast

QueueStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueueStatus) -> str:
    return value


def deserialize_json(data: str) -> QueueStatus:
    return cast(QueueStatus, data)
