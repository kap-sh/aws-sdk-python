"""Generated from Smithy shape ``com.amazonaws.quicksight#NamedEntityAggType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: NamedEntityAggType) -> str:
    return value


def deserialize_json(data: str) -> NamedEntityAggType:
    return cast(NamedEntityAggType, data)
