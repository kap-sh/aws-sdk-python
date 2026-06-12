"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#SentimentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_runtime_v2.errors import DeserializationError

SentimentType: TypeAlias = Literal[
    "MIXED",
    "NEGATIVE",
    "NEUTRAL",
    "POSITIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MIXED",
        "NEGATIVE",
        "NEUTRAL",
        "POSITIVE",
    )
)


def serialize_json(value: SentimentType) -> str:
    return value


def deserialize_json(data: str) -> SentimentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SentimentType value: {data!r}")
    return cast(SentimentType, data)
