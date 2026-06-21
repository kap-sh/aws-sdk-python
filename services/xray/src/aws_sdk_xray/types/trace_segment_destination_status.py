"""Generated from Smithy shape ``com.amazonaws.xray#TraceSegmentDestinationStatus``."""

from typing import Literal, TypeAlias, cast

TraceSegmentDestinationStatus: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TraceSegmentDestinationStatus) -> str:
    return value


def deserialize_json(data: str) -> TraceSegmentDestinationStatus:
    return cast(TraceSegmentDestinationStatus, data)
