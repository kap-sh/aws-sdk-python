"""Generated from Smithy shape ``com.amazonaws.datazone#NotificationType``."""

from typing import Literal, TypeAlias, cast

NotificationType: TypeAlias = Literal[
    "TASK",
    "EVENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationType) -> str:
    return value


def deserialize_json(data: str) -> NotificationType:
    return cast(NotificationType, data)
