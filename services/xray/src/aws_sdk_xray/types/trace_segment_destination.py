"""Generated from Smithy shape ``com.amazonaws.xray#TraceSegmentDestination``."""

from typing import Literal, TypeAlias, cast

TraceSegmentDestination: TypeAlias = Literal[
    "XRay",
    "CloudWatchLogs",
]


# --- restJson1 ser/de ---
def serialize_json(value: TraceSegmentDestination) -> str:
    return value


def deserialize_json(data: str) -> TraceSegmentDestination:
    return cast(TraceSegmentDestination, data)
