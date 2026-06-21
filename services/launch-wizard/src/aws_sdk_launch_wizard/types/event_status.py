"""Generated from Smithy shape ``com.amazonaws.launchwizard#EventStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: EventStatus) -> str:
    return value


def deserialize_json(data: str) -> EventStatus:
    return cast(EventStatus, data)
