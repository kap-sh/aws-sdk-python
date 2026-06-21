"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentMetricName``."""

from typing import Literal, TypeAlias, cast

AnalyticsIntentMetricName: TypeAlias = Literal[
    "Count",
    "Success",
    "Failure",
    "Switched",
    "Dropped",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentMetricName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsIntentMetricName:
    return cast(AnalyticsIntentMetricName, data)
