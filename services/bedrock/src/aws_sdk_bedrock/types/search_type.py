"""Generated from Smithy shape ``com.amazonaws.bedrock#SearchType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

SearchType: TypeAlias = Literal[
    "HYBRID",
    "SEMANTIC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HYBRID",
        "SEMANTIC",
    )
)


def serialize_json(value: SearchType) -> str:
    return value


def deserialize_json(data: str) -> SearchType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchType value: {data!r}")
    return cast(SearchType, data)
