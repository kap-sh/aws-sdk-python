"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#ImageError``."""

from typing import Literal, TypeAlias, cast

ImageError: TypeAlias = Literal[
    "NO_MEDIA",
    "MEDIA_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageError) -> str:
    return value


def deserialize_json(data: str) -> ImageError:
    return cast(ImageError, data)
