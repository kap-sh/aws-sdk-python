"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaPipelineElementStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "NotStarted",
        "NotSupported",
        "Initializing",
        "InProgress",
        "Failed",
        "Stopping",
        "Stopped",
        "Paused",
    )
)


def serialize_json(value: MediaPipelineElementStatus) -> str:
    return value


def deserialize_json(data: str) -> MediaPipelineElementStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MediaPipelineElementStatus value: {data!r}"
        )
    return cast(MediaPipelineElementStatus, data)
