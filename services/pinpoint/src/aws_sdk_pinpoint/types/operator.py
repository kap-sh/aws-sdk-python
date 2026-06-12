"""Generated from Smithy shape ``com.amazonaws.pinpoint#Operator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

Operator: TypeAlias = Literal[
    "ALL",
    "ANY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "ANY",
    )
)


def serialize_json(value: Operator) -> str:
    return value


def deserialize_json(data: str) -> Operator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Operator value: {data!r}")
    return cast(Operator, data)
