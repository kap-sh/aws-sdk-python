"""Generated from Smithy shape ``com.amazonaws.medialive#AudioOnlyHlsSegmentType``."""

from typing import Literal, TypeAlias, cast

"""Audio Only Hls Segment Type"""
AudioOnlyHlsSegmentType: TypeAlias = Literal[
    "AAC",
    "FMP4",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioOnlyHlsSegmentType) -> str:
    return value


def deserialize_json(data: str) -> AudioOnlyHlsSegmentType:
    return cast(AudioOnlyHlsSegmentType, data)
