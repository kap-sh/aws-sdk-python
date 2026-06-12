"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#ImageError``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video_archived_media.errors import DeserializationError

ImageError: TypeAlias = Literal[
    "NO_MEDIA",
    "MEDIA_ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_MEDIA",
        "MEDIA_ERROR",
    )
)


def serialize_json(value: ImageError) -> str:
    return value


def deserialize_json(data: str) -> ImageError:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageError value: {data!r}")
    return cast(ImageError, data)
