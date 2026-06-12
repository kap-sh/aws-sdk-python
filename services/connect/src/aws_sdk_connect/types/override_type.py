"""Generated from Smithy shape ``com.amazonaws.connect#OverrideType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

OverrideType: TypeAlias = Literal[
    "STANDARD",
    "OPEN",
    "CLOSED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "OPEN",
        "CLOSED",
    )
)


def serialize_json(value: OverrideType) -> str:
    return value


def deserialize_json(data: str) -> OverrideType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OverrideType value: {data!r}")
    return cast(OverrideType, data)
