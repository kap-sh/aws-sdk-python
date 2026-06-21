"""Generated from Smithy shape ``com.amazonaws.xray#TimeRangeType``."""

from typing import Literal, TypeAlias, cast

TimeRangeType: TypeAlias = Literal[
    "TraceId",
    "Event",
    "Service",
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeRangeType) -> str:
    return value


def deserialize_json(data: str) -> TimeRangeType:
    return cast(TimeRangeType, data)
