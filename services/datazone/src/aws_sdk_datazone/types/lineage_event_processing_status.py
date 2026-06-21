"""Generated from Smithy shape ``com.amazonaws.datazone#LineageEventProcessingStatus``."""

from typing import Literal, TypeAlias, cast

LineageEventProcessingStatus: TypeAlias = Literal[
    "REQUESTED",
    "PROCESSING",
    "SUCCESS",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: LineageEventProcessingStatus) -> str:
    return value


def deserialize_json(data: str) -> LineageEventProcessingStatus:
    return cast(LineageEventProcessingStatus, data)
