"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#HLSDisplayFragmentTimestamp``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video_archived_media.errors import DeserializationError

HLSDisplayFragmentTimestamp: TypeAlias = Literal[
    "ALWAYS",
    "NEVER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALWAYS",
        "NEVER",
    )
)


def serialize_json(value: HLSDisplayFragmentTimestamp) -> str:
    return value


def deserialize_json(data: str) -> HLSDisplayFragmentTimestamp:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown HLSDisplayFragmentTimestamp value: {data!r}"
        )
    return cast(HLSDisplayFragmentTimestamp, data)
