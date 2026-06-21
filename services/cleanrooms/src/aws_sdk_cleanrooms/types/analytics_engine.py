"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalyticsEngine``."""

from typing import Literal, TypeAlias, cast

AnalyticsEngine: TypeAlias = Literal[
    "SPARK",
    "CLEAN_ROOMS_SQL",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsEngine) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsEngine:
    return cast(AnalyticsEngine, data)
