"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalyticsEngine``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

AnalyticsEngine: TypeAlias = Literal[
    "SPARK",
    "CLEAN_ROOMS_SQL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SPARK",
        "CLEAN_ROOMS_SQL",
    )
)


def serialize_json(value: AnalyticsEngine) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsEngine:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalyticsEngine value: {data!r}")
    return cast(AnalyticsEngine, data)
