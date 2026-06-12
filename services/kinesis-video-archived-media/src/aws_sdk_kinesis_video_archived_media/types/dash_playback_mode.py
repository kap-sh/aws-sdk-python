"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#DASHPlaybackMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video_archived_media.errors import DeserializationError

DASHPlaybackMode: TypeAlias = Literal[
    "LIVE",
    "LIVE_REPLAY",
    "ON_DEMAND",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LIVE",
        "LIVE_REPLAY",
        "ON_DEMAND",
    )
)


def serialize_json(value: DASHPlaybackMode) -> str:
    return value


def deserialize_json(data: str) -> DASHPlaybackMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DASHPlaybackMode value: {data!r}")
    return cast(DASHPlaybackMode, data)
