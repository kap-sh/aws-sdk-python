"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#SentimentValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect_contact_lens.errors import DeserializationError

SentimentValue: TypeAlias = Literal[
    "POSITIVE",
    "NEUTRAL",
    "NEGATIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "POSITIVE",
        "NEUTRAL",
        "NEGATIVE",
    )
)


def serialize_json(value: SentimentValue) -> str:
    return value


def deserialize_json(data: str) -> SentimentValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SentimentValue value: {data!r}")
    return cast(SentimentValue, data)
