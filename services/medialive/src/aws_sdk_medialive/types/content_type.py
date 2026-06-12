"""Generated from Smithy shape ``com.amazonaws.medialive#ContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Specifies the media type of the thumbnail."""
ContentType: TypeAlias = Literal["image/jpeg",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("image/jpeg",))


def serialize_json(value: ContentType) -> str:
    return value


def deserialize_json(data: str) -> ContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentType value: {data!r}")
    return cast(ContentType, data)
