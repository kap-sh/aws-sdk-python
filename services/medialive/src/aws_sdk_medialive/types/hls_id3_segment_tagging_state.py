"""Generated from Smithy shape ``com.amazonaws.medialive#HlsId3SegmentTaggingState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""State of HLS ID3 Segment Tagging"""
HlsId3SegmentTaggingState: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: HlsId3SegmentTaggingState) -> str:
    return value


def deserialize_json(data: str) -> HlsId3SegmentTaggingState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsId3SegmentTaggingState value: {data!r}")
    return cast(HlsId3SegmentTaggingState, data)
