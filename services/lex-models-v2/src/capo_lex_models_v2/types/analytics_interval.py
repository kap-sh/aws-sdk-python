"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsInterval``."""

from typing import Literal, TypeAlias, cast

AnalyticsInterval: TypeAlias = Literal[
    "OneHour",
    "OneDay",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsInterval) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsInterval:
    return cast(AnalyticsInterval, data)
