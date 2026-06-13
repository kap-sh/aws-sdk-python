"""Generated from Smithy shape ``com.amazonaws.quicksight#NamedEntityAggType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

NamedEntityAggType: TypeAlias = Literal[
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
        "CUSTOM",
    )
)


def serialize_json(value: NamedEntityAggType) -> str:
    return value


def deserialize_json(data: str) -> NamedEntityAggType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NamedEntityAggType value: {data!r}")
    return cast(NamedEntityAggType, data)
