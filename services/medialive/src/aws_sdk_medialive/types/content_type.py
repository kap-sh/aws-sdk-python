"""Generated from Smithy shape ``com.amazonaws.medialive#ContentType``."""

from typing import Literal, TypeAlias, cast

"""Specifies the media type of the thumbnail."""
ContentType: TypeAlias = Literal["image/jpeg",]


# --- restJson1 ser/de ---
def serialize_json(value: ContentType) -> str:
    return value


def deserialize_json(data: str) -> ContentType:
    return cast(ContentType, data)
