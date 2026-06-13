"""Generated from Smithy shape ``com.amazonaws.launchwizard#EventStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_launch_wizard.errors import DeserializationError

EventStatus: TypeAlias = Literal[
    "CANCELED",
    "CANCELING",
    "COMPLETED",
    "CREATED",
    "FAILED",
    "IN_PROGRESS",
    "PENDING",
    "TIMED_OUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CANCELED",
        "CANCELING",
        "COMPLETED",
        "CREATED",
        "FAILED",
        "IN_PROGRESS",
        "PENDING",
        "TIMED_OUT",
    )
)


def serialize_json(value: EventStatus) -> str:
    return value


def deserialize_json(data: str) -> EventStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventStatus value: {data!r}")
    return cast(EventStatus, data)
