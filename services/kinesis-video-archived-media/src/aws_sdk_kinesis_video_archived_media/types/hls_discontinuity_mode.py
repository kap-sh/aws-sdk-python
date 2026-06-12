"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#HLSDiscontinuityMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video_archived_media.errors import DeserializationError

HLSDiscontinuityMode: TypeAlias = Literal[
    "ALWAYS",
    "NEVER",
    "ON_DISCONTINUITY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALWAYS",
        "NEVER",
        "ON_DISCONTINUITY",
    )
)


def serialize_json(value: HLSDiscontinuityMode) -> str:
    return value


def deserialize_json(data: str) -> HLSDiscontinuityMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HLSDiscontinuityMode value: {data!r}")
    return cast(HLSDiscontinuityMode, data)
