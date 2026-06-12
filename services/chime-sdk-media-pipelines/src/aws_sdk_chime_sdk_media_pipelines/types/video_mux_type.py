"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#VideoMuxType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

VideoMuxType: TypeAlias = Literal["VideoOnly",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("VideoOnly",))


def serialize_json(value: VideoMuxType) -> str:
    return value


def deserialize_json(data: str) -> VideoMuxType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VideoMuxType value: {data!r}")
    return cast(VideoMuxType, data)
