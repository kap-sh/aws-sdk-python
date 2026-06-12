"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaPipelineTaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

MediaPipelineTaskStatus: TypeAlias = Literal[
    "NotStarted",
    "Initializing",
    "InProgress",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NotStarted",
        "Initializing",
        "InProgress",
        "Failed",
        "Stopping",
        "Stopped",
    )
)


def serialize_json(value: MediaPipelineTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> MediaPipelineTaskStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MediaPipelineTaskStatus value: {data!r}")
    return cast(MediaPipelineTaskStatus, data)
