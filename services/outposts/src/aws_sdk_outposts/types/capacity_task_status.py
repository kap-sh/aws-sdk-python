"""Generated from Smithy shape ``com.amazonaws.outposts#CapacityTaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

CapacityTaskStatus: TypeAlias = Literal[
    "REQUESTED",
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
    "WAITING_FOR_EVACUATION",
    "CANCELLATION_IN_PROGRESS",
    "CANCELLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUESTED",
        "IN_PROGRESS",
        "FAILED",
        "COMPLETED",
        "WAITING_FOR_EVACUATION",
        "CANCELLATION_IN_PROGRESS",
        "CANCELLED",
    )
)


def serialize_json(value: CapacityTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> CapacityTaskStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapacityTaskStatus value: {data!r}")
    return cast(CapacityTaskStatus, data)
