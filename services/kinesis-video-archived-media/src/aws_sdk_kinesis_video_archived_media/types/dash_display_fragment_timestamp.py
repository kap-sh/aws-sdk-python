"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#DASHDisplayFragmentTimestamp``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video_archived_media.errors import DeserializationError

DASHDisplayFragmentTimestamp: TypeAlias = Literal[
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


def serialize_json(value: DASHDisplayFragmentTimestamp) -> str:
    return value


def deserialize_json(data: str) -> DASHDisplayFragmentTimestamp:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DASHDisplayFragmentTimestamp value: {data!r}"
        )
    return cast(DASHDisplayFragmentTimestamp, data)
