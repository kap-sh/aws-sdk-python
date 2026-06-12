"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsMetricStatistic``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsMetricStatistic: TypeAlias = Literal[
    "Sum",
    "Avg",
    "Max",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Sum",
        "Avg",
        "Max",
    )
)


def serialize_json(value: AnalyticsMetricStatistic) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsMetricStatistic:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalyticsMetricStatistic value: {data!r}")
    return cast(AnalyticsMetricStatistic, data)
