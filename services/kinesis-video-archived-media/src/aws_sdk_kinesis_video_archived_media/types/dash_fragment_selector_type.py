"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#DASHFragmentSelectorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video_archived_media.errors import DeserializationError

DASHFragmentSelectorType: TypeAlias = Literal[
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


def serialize_json(value: DASHFragmentSelectorType) -> str:
    return value


def deserialize_json(data: str) -> DASHFragmentSelectorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DASHFragmentSelectorType value: {data!r}")
    return cast(DASHFragmentSelectorType, data)
