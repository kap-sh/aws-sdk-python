"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsUtteranceMetricName: TypeAlias = Literal[
    "Count",
    "Missed",
    "Detected",
    "UtteranceTimestamp",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Count",
        "Missed",
        "Detected",
        "UtteranceTimestamp",
    )
)


def serialize_json(value: AnalyticsUtteranceMetricName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsUtteranceMetricName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AnalyticsUtteranceMetricName value: {data!r}"
        )
    return cast(AnalyticsUtteranceMetricName, data)
