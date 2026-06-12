"""Generated from Smithy shape ``com.amazonaws.mediatailor#EventName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

EventName: TypeAlias = Literal[
    "PRE_SESSION_INITIALIZATION",
    "PRE_ADS_REQUEST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRE_SESSION_INITIALIZATION",
        "PRE_ADS_REQUEST",
    )
)


def serialize_json(value: EventName) -> str:
    return value


def deserialize_json(data: str) -> EventName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventName value: {data!r}")
    return cast(EventName, data)
