"""Generated from Smithy shape ``com.amazonaws.outposts#CapacityTaskStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: CapacityTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> CapacityTaskStatus:
    return cast(CapacityTaskStatus, data)
