"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaPipelineSinkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

MediaPipelineSinkType: TypeAlias = Literal["S3Bucket",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("S3Bucket",))


def serialize_json(value: MediaPipelineSinkType) -> str:
    return value


def deserialize_json(data: str) -> MediaPipelineSinkType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MediaPipelineSinkType value: {data!r}")
    return cast(MediaPipelineSinkType, data)
