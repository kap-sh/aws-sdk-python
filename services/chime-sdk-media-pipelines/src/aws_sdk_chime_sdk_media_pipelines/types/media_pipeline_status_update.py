"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaPipelineStatusUpdate``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

MediaPipelineStatusUpdate: TypeAlias = Literal[
    "Pause",
    "Resume",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pause",
        "Resume",
    )
)


def serialize_json(value: MediaPipelineStatusUpdate) -> str:
    return value


def deserialize_json(data: str) -> MediaPipelineStatusUpdate:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MediaPipelineStatusUpdate value: {data!r}")
    return cast(MediaPipelineStatusUpdate, data)
