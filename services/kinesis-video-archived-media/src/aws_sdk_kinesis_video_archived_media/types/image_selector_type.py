"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#ImageSelectorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video_archived_media.errors import DeserializationError

ImageSelectorType: TypeAlias = Literal[
    "PRODUCER_TIMESTAMP",
    "SERVER_TIMESTAMP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRODUCER_TIMESTAMP",
        "SERVER_TIMESTAMP",
    )
)


def serialize_json(value: ImageSelectorType) -> str:
    return value


def deserialize_json(data: str) -> ImageSelectorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageSelectorType value: {data!r}")
    return cast(ImageSelectorType, data)
