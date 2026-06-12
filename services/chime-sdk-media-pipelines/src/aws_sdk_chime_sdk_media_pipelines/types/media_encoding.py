"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaEncoding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

MediaEncoding: TypeAlias = Literal["pcm",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("pcm",))


def serialize_json(value: MediaEncoding) -> str:
    return value


def deserialize_json(data: str) -> MediaEncoding:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MediaEncoding value: {data!r}")
    return cast(MediaEncoding, data)
