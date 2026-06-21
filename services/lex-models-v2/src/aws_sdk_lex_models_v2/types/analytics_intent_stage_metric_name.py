"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentStageMetricName``."""

from typing import Literal, TypeAlias, cast

AnalyticsIntentStageMetricName: TypeAlias = Literal[
    "Count",
    "Success",
    "Failed",
    "Dropped",
    "Retry",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentStageMetricName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsIntentStageMetricName:
    return cast(AnalyticsIntentStageMetricName, data)
