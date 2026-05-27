"""Generated from Smithy shape ``com.amazonaws.lambda#EventSourcePosition``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_lambda.errors import DeserializationError

EventSourcePosition: TypeAlias = Literal[
    "TRIM_HORIZON",
    "LATEST",
    "AT_TIMESTAMP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRIM_HORIZON",
        "LATEST",
        "AT_TIMESTAMP",
    )
)


def serialize_json(value: EventSourcePosition) -> str:
    return value


def deserialize_json(data: str) -> EventSourcePosition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventSourcePosition value: {data!r}")
    return cast(EventSourcePosition, data)
