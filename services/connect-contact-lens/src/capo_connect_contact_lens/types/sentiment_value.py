"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#SentimentValue``."""

from typing import Literal, TypeAlias, cast

SentimentValue: TypeAlias = Literal[
    "POSITIVE",
    "NEUTRAL",
    "NEGATIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SentimentValue) -> str:
    return value


def deserialize_json(data: str) -> SentimentValue:
    return cast(SentimentValue, data)
