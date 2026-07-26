"""Generated from Smithy shape ``com.amazonaws.medialive#SmoothGroupEventIdMode``."""

from typing import Literal, TypeAlias, cast

"""Smooth Group Event Id Mode"""
SmoothGroupEventIdMode: TypeAlias = Literal[
    "NO_EVENT_ID",
    "USE_CONFIGURED",
    "USE_TIMESTAMP",
]


# --- restJson1 ser/de ---
def serialize_json(value: SmoothGroupEventIdMode) -> str:
    return value


def deserialize_json(data: str) -> SmoothGroupEventIdMode:
    return cast(SmoothGroupEventIdMode, data)
