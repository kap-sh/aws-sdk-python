"""Generated from Smithy shape ``com.amazonaws.pinpoint#State``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

State: TypeAlias = Literal[
    "DRAFT",
    "ACTIVE",
    "COMPLETED",
    "CANCELLED",
    "CLOSED",
    "PAUSED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DRAFT",
        "ACTIVE",
        "COMPLETED",
        "CANCELLED",
        "CLOSED",
        "PAUSED",
    )
)


def serialize_json(value: State) -> str:
    return value


def deserialize_json(data: str) -> State:
    if data not in _VALUES:
        raise DeserializationError(f"unknown State value: {data!r}")
    return cast(State, data)
