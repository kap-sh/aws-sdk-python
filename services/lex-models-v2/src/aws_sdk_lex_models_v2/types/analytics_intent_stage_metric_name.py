"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentStageMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsIntentStageMetricName: TypeAlias = Literal[
    "Count",
    "Success",
    "Failed",
    "Dropped",
    "Retry",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Count",
        "Success",
        "Failed",
        "Dropped",
        "Retry",
    )
)


def serialize_json(value: AnalyticsIntentStageMetricName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsIntentStageMetricName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AnalyticsIntentStageMetricName value: {data!r}"
        )
    return cast(AnalyticsIntentStageMetricName, data)
