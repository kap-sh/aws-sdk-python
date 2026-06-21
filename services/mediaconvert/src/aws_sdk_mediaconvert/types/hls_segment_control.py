"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsSegmentControl``."""

from typing import Literal, TypeAlias, cast

"""When set to SINGLE_FILE, emits program as a single media resource (.ts) file, uses #EXT-X-BYTERANGE tags to index segment for playback."""
HlsSegmentControl: TypeAlias = Literal[
    "SINGLE_FILE",
    "SEGMENTED_FILES",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsSegmentControl) -> str:
    return value


def deserialize_json(data: str) -> HlsSegmentControl:
    return cast(HlsSegmentControl, data)
