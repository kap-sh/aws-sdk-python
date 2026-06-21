"""Generated from Smithy shape ``com.amazonaws.quicksight#AggType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: AggType) -> str:
    return value


def deserialize_json(data: str) -> AggType:
    return cast(AggType, data)
