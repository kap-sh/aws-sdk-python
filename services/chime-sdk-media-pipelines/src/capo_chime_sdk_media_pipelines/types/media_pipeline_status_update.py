"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaPipelineStatusUpdate``."""

from typing import Literal, TypeAlias, cast

MediaPipelineStatusUpdate: TypeAlias = Literal[
    "Pause",
    "Resume",
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaPipelineStatusUpdate) -> str:
    return value


def deserialize_json(data: str) -> MediaPipelineStatusUpdate:
    return cast(MediaPipelineStatusUpdate, data)
