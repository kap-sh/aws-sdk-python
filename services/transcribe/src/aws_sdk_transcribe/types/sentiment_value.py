"""Generated from Smithy shape ``com.amazonaws.transcribe#SentimentValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

SentimentValue: TypeAlias = Literal[
    "POSITIVE",
    "NEGATIVE",
    "NEUTRAL",
    "MIXED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "POSITIVE",
        "NEGATIVE",
        "NEUTRAL",
        "MIXED",
    )
)


def serialize_aws_json_1_1(value: SentimentValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SentimentValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SentimentValue value: {data!r}")
    return cast(SentimentValue, data)
