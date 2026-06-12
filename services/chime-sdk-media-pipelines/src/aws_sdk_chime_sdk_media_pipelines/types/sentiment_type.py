"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#SentimentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

SentimentType: TypeAlias = Literal["NEGATIVE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("NEGATIVE",))


def serialize_json(value: SentimentType) -> str:
    return value


def deserialize_json(data: str) -> SentimentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SentimentType value: {data!r}")
    return cast(SentimentType, data)
