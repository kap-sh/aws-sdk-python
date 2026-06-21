"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventStreamDestinationStatus``."""

from typing import Literal, TypeAlias, cast

EventStreamDestinationStatus: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventStreamDestinationStatus) -> str:
    return value


def deserialize_json(data: str) -> EventStreamDestinationStatus:
    return cast(EventStreamDestinationStatus, data)
