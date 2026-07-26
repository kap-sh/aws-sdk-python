"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#Sentiment``."""

from typing import Literal, TypeAlias, cast

Sentiment: TypeAlias = Literal[
    "POSITIVE",
    "NEGATIVE",
    "MIXED",
    "NEUTRAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: Sentiment) -> str:
    return value


def deserialize_json(data: str) -> Sentiment:
    return cast(Sentiment, data)
