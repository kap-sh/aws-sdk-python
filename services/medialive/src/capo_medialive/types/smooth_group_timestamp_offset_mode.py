"""Generated from Smithy shape ``com.amazonaws.medialive#SmoothGroupTimestampOffsetMode``."""

from typing import Literal, TypeAlias, cast

"""Smooth Group Timestamp Offset Mode"""
SmoothGroupTimestampOffsetMode: TypeAlias = Literal[
    "USE_CONFIGURED_OFFSET",
    "USE_EVENT_START_DATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SmoothGroupTimestampOffsetMode) -> str:
    return value


def deserialize_json(data: str) -> SmoothGroupTimestampOffsetMode:
    return cast(SmoothGroupTimestampOffsetMode, data)
