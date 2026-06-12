"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisSentimentLabel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

RealTimeContactAnalysisSentimentLabel: TypeAlias = Literal[
    "POSITIVE",
    "NEGATIVE",
    "NEUTRAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "POSITIVE",
        "NEGATIVE",
        "NEUTRAL",
    )
)


def serialize_json(value: RealTimeContactAnalysisSentimentLabel) -> str:
    return value


def deserialize_json(data: str) -> RealTimeContactAnalysisSentimentLabel:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RealTimeContactAnalysisSentimentLabel value: {data!r}"
        )
    return cast(RealTimeContactAnalysisSentimentLabel, data)
