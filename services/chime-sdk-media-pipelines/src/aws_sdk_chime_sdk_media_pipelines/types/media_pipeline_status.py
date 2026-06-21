"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaPipelineStatus``."""

from typing import Literal, TypeAlias, cast

MediaPipelineStatus: TypeAlias = Literal[
    "Initializing",
    "InProgress",
    "Failed",
    "Stopping",
    "Stopped",
    "Paused",
    "NotStarted",
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaPipelineStatus) -> str:
    return value


def deserialize_json(data: str) -> MediaPipelineStatus:
    return cast(MediaPipelineStatus, data)
