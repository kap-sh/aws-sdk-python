"""Generated from Smithy shape ``com.amazonaws.deadline#SearchTermMatchingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

SearchTermMatchingType: TypeAlias = Literal[
    "FUZZY_MATCH",
    "CONTAINS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FUZZY_MATCH",
        "CONTAINS",
    )
)


def serialize_json(value: SearchTermMatchingType) -> str:
    return value


def deserialize_json(data: str) -> SearchTermMatchingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchTermMatchingType value: {data!r}")
    return cast(SearchTermMatchingType, data)
