"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventStreamDestinationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

EventStreamDestinationStatus: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEALTHY",
        "UNHEALTHY",
    )
)


def serialize_json(value: EventStreamDestinationStatus) -> str:
    return value


def deserialize_json(data: str) -> EventStreamDestinationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EventStreamDestinationStatus value: {data!r}"
        )
    return cast(EventStreamDestinationStatus, data)
