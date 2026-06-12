"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

ContentType: TypeAlias = Literal["PII",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PII",))


def serialize_json(value: ContentType) -> str:
    return value


def deserialize_json(data: str) -> ContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentType value: {data!r}")
    return cast(ContentType, data)
