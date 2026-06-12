"""Generated from Smithy shape ``com.amazonaws.pinpoint#FilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

FilterType: TypeAlias = Literal[
    "SYSTEM",
    "ENDPOINT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SYSTEM",
        "ENDPOINT",
    )
)


def serialize_json(value: FilterType) -> str:
    return value


def deserialize_json(data: str) -> FilterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterType value: {data!r}")
    return cast(FilterType, data)
