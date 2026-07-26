"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaPipelineTaskStatus``."""

from typing import Literal, TypeAlias, cast

MediaPipelineTaskStatus: TypeAlias = Literal[
    "NotStarted",
    "Initializing",
    "InProgress",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaPipelineTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> MediaPipelineTaskStatus:
    return cast(MediaPipelineTaskStatus, data)
