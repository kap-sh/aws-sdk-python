"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSessionMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsSessionMetricName: TypeAlias = Literal[
    "Count",
    "Success",
    "Failure",
    "Dropped",
    "Duration",
    "TurnsPerConversation",
    "Concurrency",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Count",
        "Success",
        "Failure",
        "Dropped",
        "Duration",
        "TurnsPerConversation",
        "Concurrency",
    )
)


def serialize_json(value: AnalyticsSessionMetricName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsSessionMetricName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AnalyticsSessionMetricName value: {data!r}"
        )
    return cast(AnalyticsSessionMetricName, data)
