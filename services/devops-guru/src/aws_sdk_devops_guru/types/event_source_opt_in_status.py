"""Generated from Smithy shape ``com.amazonaws.devopsguru#EventSourceOptInStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

EventSourceOptInStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: EventSourceOptInStatus) -> str:
    return value


def deserialize_json(data: str) -> EventSourceOptInStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventSourceOptInStatus value: {data!r}")
    return cast(EventSourceOptInStatus, data)
