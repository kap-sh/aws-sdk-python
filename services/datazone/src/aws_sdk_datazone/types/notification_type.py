"""Generated from Smithy shape ``com.amazonaws.datazone#NotificationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

NotificationType: TypeAlias = Literal[
    "TASK",
    "EVENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TASK",
        "EVENT",
    )
)


def serialize_json(value: NotificationType) -> str:
    return value


def deserialize_json(data: str) -> NotificationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotificationType value: {data!r}")
    return cast(NotificationType, data)
