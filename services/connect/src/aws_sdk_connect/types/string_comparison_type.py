"""Generated from Smithy shape ``com.amazonaws.connect#StringComparisonType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

StringComparisonType: TypeAlias = Literal[
    "STARTS_WITH",
    "CONTAINS",
    "EXACT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTS_WITH",
        "CONTAINS",
        "EXACT",
    )
)


def serialize_json(value: StringComparisonType) -> str:
    return value


def deserialize_json(data: str) -> StringComparisonType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StringComparisonType value: {data!r}")
    return cast(StringComparisonType, data)
