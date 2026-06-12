"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#ContainerFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video_archived_media.errors import DeserializationError

ContainerFormat: TypeAlias = Literal[
    "FRAGMENTED_MP4",
    "MPEG_TS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FRAGMENTED_MP4",
        "MPEG_TS",
    )
)


def serialize_json(value: ContainerFormat) -> str:
    return value


def deserialize_json(data: str) -> ContainerFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContainerFormat value: {data!r}")
    return cast(ContainerFormat, data)
