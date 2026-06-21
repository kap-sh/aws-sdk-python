"""Generated from Smithy shape ``com.amazonaws.deadline#SessionsStatisticsAggregationStatus``."""

from typing import Literal, TypeAlias, cast

SessionsStatisticsAggregationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "TIMEOUT",
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionsStatisticsAggregationStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionsStatisticsAggregationStatus:
    return cast(SessionsStatisticsAggregationStatus, data)
