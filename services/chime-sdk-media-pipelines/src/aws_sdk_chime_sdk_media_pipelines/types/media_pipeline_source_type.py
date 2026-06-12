"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaPipelineSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

MediaPipelineSourceType: TypeAlias = Literal["ChimeSdkMeeting",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ChimeSdkMeeting",))


def serialize_json(value: MediaPipelineSourceType) -> str:
    return value


def deserialize_json(data: str) -> MediaPipelineSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MediaPipelineSourceType value: {data!r}")
    return cast(MediaPipelineSourceType, data)
