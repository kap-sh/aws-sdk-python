"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#SentimentType``."""

from typing import Literal, TypeAlias, cast

SentimentType: TypeAlias = Literal[
    "MIXED",
    "NEGATIVE",
    "NEUTRAL",
    "POSITIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SentimentType) -> str:
    return value


def deserialize_json(data: str) -> SentimentType:
    return cast(SentimentType, data)
