"""Generated from Smithy shape ``com.amazonaws.opensearch#ScheduledBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

ScheduledBy: TypeAlias = Literal[
    "CUSTOMER",
    "SYSTEM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER",
        "SYSTEM",
    )
)


def serialize_json(value: ScheduledBy) -> str:
    return value


def deserialize_json(data: str) -> ScheduledBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScheduledBy value: {data!r}")
    return cast(ScheduledBy, data)
