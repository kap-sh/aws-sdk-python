"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaPipelineStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "Initializing",
        "InProgress",
        "Failed",
        "Stopping",
        "Stopped",
        "Paused",
        "NotStarted",
    )
)


def serialize_json(value: MediaPipelineStatus) -> str:
    return value


def deserialize_json(data: str) -> MediaPipelineStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MediaPipelineStatus value: {data!r}")
    return cast(MediaPipelineStatus, data)
