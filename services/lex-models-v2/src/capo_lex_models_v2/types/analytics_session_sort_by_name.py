"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSessionSortByName``."""

from typing import Literal, TypeAlias, cast

AnalyticsSessionSortByName: TypeAlias = Literal[
    "ConversationStartTime",
    "NumberOfTurns",
    "Duration",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsSessionSortByName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsSessionSortByName:
    return cast(AnalyticsSessionSortByName, data)
