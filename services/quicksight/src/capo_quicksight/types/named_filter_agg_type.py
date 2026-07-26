"""Generated from Smithy shape ``com.amazonaws.quicksight#NamedFilterAggType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: NamedFilterAggType) -> str:
    return value


def deserialize_json(data: str) -> NamedFilterAggType:
    return cast(NamedFilterAggType, data)
