"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#SentimentType``."""

from typing import Literal, TypeAlias, cast

SentimentType: TypeAlias = Literal["NEGATIVE",]


# --- restJson1 ser/de ---
def serialize_json(value: SentimentType) -> str:
    return value


def deserialize_json(data: str) -> SentimentType:
    return cast(SentimentType, data)
