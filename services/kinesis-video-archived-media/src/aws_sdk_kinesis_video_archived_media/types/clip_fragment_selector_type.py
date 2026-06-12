"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#ClipFragmentSelectorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video_archived_media.errors import DeserializationError

ClipFragmentSelectorType: TypeAlias = Literal[
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


def serialize_json(value: ClipFragmentSelectorType) -> str:
    return value


def deserialize_json(data: str) -> ClipFragmentSelectorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClipFragmentSelectorType value: {data!r}")
    return cast(ClipFragmentSelectorType, data)
