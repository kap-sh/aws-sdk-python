"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ContentMuxType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

ContentMuxType: TypeAlias = Literal["ContentOnly",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ContentOnly",))


def serialize_json(value: ContentMuxType) -> str:
    return value


def deserialize_json(data: str) -> ContentMuxType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentMuxType value: {data!r}")
    return cast(ContentMuxType, data)
