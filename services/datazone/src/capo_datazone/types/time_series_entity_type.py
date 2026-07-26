"""Generated from Smithy shape ``com.amazonaws.datazone#TimeSeriesEntityType``."""

from typing import Literal, TypeAlias, cast

TimeSeriesEntityType: TypeAlias = Literal[
    "ASSET",
    "LISTING",
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeSeriesEntityType) -> str:
    return value


def deserialize_json(data: str) -> TimeSeriesEntityType:
    return cast(TimeSeriesEntityType, data)
