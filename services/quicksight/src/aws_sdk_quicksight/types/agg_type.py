"""Generated from Smithy shape ``com.amazonaws.quicksight#AggType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AggType: TypeAlias = Literal[
    "SUM",
    "MIN",
    "MAX",
    "COUNT",
    "AVERAGE",
    "DISTINCT_COUNT",
    "STDEV",
    "STDEVP",
    "VAR",
    "VARP",
    "PERCENTILE",
    "MEDIAN",
    "PTD_SUM",
    "PTD_MIN",
    "PTD_MAX",
    "PTD_COUNT",
    "PTD_DISTINCT_COUNT",
    "PTD_AVERAGE",
    "COLUMN",
    "CUSTOM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUM",
        "MIN",
        "MAX",
        "COUNT",
        "AVERAGE",
        "DISTINCT_COUNT",
        "STDEV",
        "STDEVP",
        "VAR",
        "VARP",
        "PERCENTILE",
        "MEDIAN",
        "PTD_SUM",
        "PTD_MIN",
        "PTD_MAX",
        "PTD_COUNT",
        "PTD_DISTINCT_COUNT",
        "PTD_AVERAGE",
        "COLUMN",
        "CUSTOM",
    )
)


def serialize_json(value: AggType) -> str:
    return value


def deserialize_json(data: str) -> AggType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AggType value: {data!r}")
    return cast(AggType, data)
