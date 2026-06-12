"""Generated from Smithy shape ``com.amazonaws.connect#SearchContactsMatchType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

SearchContactsMatchType: TypeAlias = Literal[
    "MATCH_ALL",
    "MATCH_ANY",
    "MATCH_EXACT",
    "MATCH_NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MATCH_ALL",
        "MATCH_ANY",
        "MATCH_EXACT",
        "MATCH_NONE",
    )
)


def serialize_json(value: SearchContactsMatchType) -> str:
    return value


def deserialize_json(data: str) -> SearchContactsMatchType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchContactsMatchType value: {data!r}")
    return cast(SearchContactsMatchType, data)
