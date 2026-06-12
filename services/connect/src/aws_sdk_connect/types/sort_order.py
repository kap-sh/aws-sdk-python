"""Generated from Smithy shape ``com.amazonaws.connect#SortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

SortOrder: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASCENDING",
        "DESCENDING",
    )
)


def serialize_json(value: SortOrder) -> str:
    return value


def deserialize_json(data: str) -> SortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortOrder value: {data!r}")
    return cast(SortOrder, data)
