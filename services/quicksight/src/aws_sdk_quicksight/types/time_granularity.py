"""Generated from Smithy shape ``com.amazonaws.quicksight#TimeGranularity``."""

from typing import Literal, TypeAlias, cast

TimeGranularity: TypeAlias = Literal[
    "YEAR",
    "QUARTER",
    "MONTH",
    "WEEK",
    "DAY",
    "HOUR",
    "MINUTE",
    "SECOND",
    "MILLISECOND",
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeGranularity) -> str:
    return value


def deserialize_json(data: str) -> TimeGranularity:
    return cast(TimeGranularity, data)
