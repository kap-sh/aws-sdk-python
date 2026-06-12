"""Generated from Smithy shape ``com.amazonaws.medialive#AudioOnlyHlsSegmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Audio Only Hls Segment Type"""
AudioOnlyHlsSegmentType: TypeAlias = Literal[
    "AAC",
    "FMP4",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AAC",
        "FMP4",
    )
)


def serialize_json(value: AudioOnlyHlsSegmentType) -> str:
    return value


def deserialize_json(data: str) -> AudioOnlyHlsSegmentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AudioOnlyHlsSegmentType value: {data!r}")
    return cast(AudioOnlyHlsSegmentType, data)
