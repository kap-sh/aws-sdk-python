"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaPipelineElementStatus``."""

from typing import Literal, TypeAlias, cast

MediaPipelineElementStatus: TypeAlias = Literal[
    "NotStarted",
    "NotSupported",
    "Initializing",
    "InProgress",
    "Failed",
    "Stopping",
    "Stopped",
    "Paused",
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaPipelineElementStatus) -> str:
    return value


def deserialize_json(data: str) -> MediaPipelineElementStatus:
    return cast(MediaPipelineElementStatus, data)
