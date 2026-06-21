"""Generated from Smithy shape ``com.amazonaws.medialive#PipelineLockingMethod``."""

from typing import Literal, TypeAlias, cast

"""Pipeline Locking Method"""
PipelineLockingMethod: TypeAlias = Literal[
    "SOURCE_TIMECODE",
    "VIDEO_ALIGNMENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: PipelineLockingMethod) -> str:
    return value


def deserialize_json(data: str) -> PipelineLockingMethod:
    return cast(PipelineLockingMethod, data)
