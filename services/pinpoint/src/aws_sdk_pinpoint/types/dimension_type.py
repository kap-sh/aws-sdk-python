"""Generated from Smithy shape ``com.amazonaws.pinpoint#DimensionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

DimensionType: TypeAlias = Literal[
    "INCLUSIVE",
    "EXCLUSIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUSIVE",
        "EXCLUSIVE",
    )
)


def serialize_json(value: DimensionType) -> str:
    return value


def deserialize_json(data: str) -> DimensionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DimensionType value: {data!r}")
    return cast(DimensionType, data)
