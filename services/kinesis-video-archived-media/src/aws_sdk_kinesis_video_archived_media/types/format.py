"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#Format``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video_archived_media.errors import DeserializationError

Format: TypeAlias = Literal[
    "JPEG",
    "PNG",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JPEG",
        "PNG",
    )
)


def serialize_json(value: Format) -> str:
    return value


def deserialize_json(data: str) -> Format:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Format value: {data!r}")
    return cast(Format, data)
