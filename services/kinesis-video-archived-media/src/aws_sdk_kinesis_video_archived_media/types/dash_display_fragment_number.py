"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#DASHDisplayFragmentNumber``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video_archived_media.errors import DeserializationError

DASHDisplayFragmentNumber: TypeAlias = Literal[
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


def serialize_json(value: DASHDisplayFragmentNumber) -> str:
    return value


def deserialize_json(data: str) -> DASHDisplayFragmentNumber:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DASHDisplayFragmentNumber value: {data!r}")
    return cast(DASHDisplayFragmentNumber, data)
