"""Generated from Smithy shape ``com.amazonaws.comprehend#SentimentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

SentimentType: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: SentimentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SentimentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SentimentType value: {data!r}")
    return cast(SentimentType, data)
