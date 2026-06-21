"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultAggregation``."""

from typing import Literal, TypeAlias, cast

DefaultAggregation: TypeAlias = Literal[
    "SUM",
    "MAX",
    "MIN",
    "COUNT",
    "DISTINCT_COUNT",
    "AVERAGE",
    "MEDIAN",
    "STDEV",
    "STDEVP",
    "VAR",
    "VARP",
]


# --- restJson1 ser/de ---
def serialize_json(value: DefaultAggregation) -> str:
    return value


def deserialize_json(data: str) -> DefaultAggregation:
    return cast(DefaultAggregation, data)
