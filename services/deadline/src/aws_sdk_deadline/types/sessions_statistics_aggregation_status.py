"""Generated from Smithy shape ``com.amazonaws.deadline#SessionsStatisticsAggregationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

SessionsStatisticsAggregationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "TIMEOUT",
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "TIMEOUT",
        "FAILED",
        "COMPLETED",
    )
)


def serialize_json(value: SessionsStatisticsAggregationStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionsStatisticsAggregationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SessionsStatisticsAggregationStatus value: {data!r}"
        )
    return cast(SessionsStatisticsAggregationStatus, data)
