"""Generated from Smithy shape ``com.amazonaws.quicksight#NamedFilterAggType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

NamedFilterAggType: TypeAlias = Literal[
    "NO_AGGREGATION",
    "SUM",
    "AVERAGE",
    "COUNT",
    "DISTINCT_COUNT",
    "MAX",
    "MEDIAN",
    "MIN",
    "STDEV",
    "STDEVP",
    "VAR",
    "VARP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_AGGREGATION",
        "SUM",
        "AVERAGE",
        "COUNT",
        "DISTINCT_COUNT",
        "MAX",
        "MEDIAN",
        "MIN",
        "STDEV",
        "STDEVP",
        "VAR",
        "VARP",
    )
)


def serialize_json(value: NamedFilterAggType) -> str:
    return value


def deserialize_json(data: str) -> NamedFilterAggType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NamedFilterAggType value: {data!r}")
    return cast(NamedFilterAggType, data)
