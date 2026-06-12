"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsIntentMetricName: TypeAlias = Literal[
    "Count",
    "Success",
    "Failure",
    "Switched",
    "Dropped",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Count",
        "Success",
        "Failure",
        "Switched",
        "Dropped",
    )
)


def serialize_json(value: AnalyticsIntentMetricName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsIntentMetricName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalyticsIntentMetricName value: {data!r}")
    return cast(AnalyticsIntentMetricName, data)
