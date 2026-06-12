"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsSegmentControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When set to SINGLE_FILE, emits program as a single media resource (.ts) file, uses #EXT-X-BYTERANGE tags to index segment for playback."""
HlsSegmentControl: TypeAlias = Literal[
    "SINGLE_FILE",
    "SEGMENTED_FILES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE_FILE",
        "SEGMENTED_FILES",
    )
)


def serialize_json(value: HlsSegmentControl) -> str:
    return value


def deserialize_json(data: str) -> HlsSegmentControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsSegmentControl value: {data!r}")
    return cast(HlsSegmentControl, data)
