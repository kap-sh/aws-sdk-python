"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceMetricName``."""

from typing import Literal, TypeAlias, cast

AnalyticsUtteranceMetricName: TypeAlias = Literal[
    "Count",
    "Missed",
    "Detected",
    "UtteranceTimestamp",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceMetricName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsUtteranceMetricName:
    return cast(AnalyticsUtteranceMetricName, data)
