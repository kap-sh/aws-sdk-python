"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#HLSPlaybackMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video_archived_media.errors import DeserializationError

HLSPlaybackMode: TypeAlias = Literal[
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


def serialize_json(value: HLSPlaybackMode) -> str:
    return value


def deserialize_json(data: str) -> HLSPlaybackMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HLSPlaybackMode value: {data!r}")
    return cast(HLSPlaybackMode, data)
