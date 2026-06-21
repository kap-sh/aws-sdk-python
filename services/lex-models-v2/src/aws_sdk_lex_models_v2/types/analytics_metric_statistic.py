"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsMetricStatistic``."""

from typing import Literal, TypeAlias, cast

AnalyticsMetricStatistic: TypeAlias = Literal[
    "Sum",
    "Avg",
    "Max",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsMetricStatistic) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsMetricStatistic:
    return cast(AnalyticsMetricStatistic, data)
