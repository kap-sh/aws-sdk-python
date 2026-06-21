"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSessionMetricName``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: AnalyticsSessionMetricName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsSessionMetricName:
    return cast(AnalyticsSessionMetricName, data)
