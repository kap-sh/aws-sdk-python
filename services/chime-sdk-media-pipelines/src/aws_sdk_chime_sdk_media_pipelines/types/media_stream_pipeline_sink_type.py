"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaStreamPipelineSinkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

MediaStreamPipelineSinkType: TypeAlias = Literal["KinesisVideoStreamPool",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("KinesisVideoStreamPool",))


def serialize_json(value: MediaStreamPipelineSinkType) -> str:
    return value


def deserialize_json(data: str) -> MediaStreamPipelineSinkType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MediaStreamPipelineSinkType value: {data!r}"
        )
    return cast(MediaStreamPipelineSinkType, data)
