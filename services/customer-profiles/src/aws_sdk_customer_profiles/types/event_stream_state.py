"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventStreamState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

EventStreamState: TypeAlias = Literal[
    "RUNNING",
    "STOPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "STOPPED",
    )
)


def serialize_json(value: EventStreamState) -> str:
    return value


def deserialize_json(data: str) -> EventStreamState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventStreamState value: {data!r}")
    return cast(EventStreamState, data)
