"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DolbyVisionCompatibility``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When you set Compatibility mapping to Duplicate Stream, DolbyVision streams that have a backward compatible base layer (e.g., DolbyVision 8.1) will cause a duplicate stream to be signaled in the manifest as a duplicate stream. When you set Compatibility mapping to Supplemntal Codecs, DolbyVision streams that have a backward compatible base layer (e.g., DolbyVision 8.1) will cause the associate stream in the manifest to include a SUPPLEMENTAL_CODECS property."""
DolbyVisionCompatibility: TypeAlias = Literal[
    "DUPLICATE_STREAM",
    "SUPPLEMENTAL_CODECS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DUPLICATE_STREAM",
        "SUPPLEMENTAL_CODECS",
    )
)


def serialize_json(value: DolbyVisionCompatibility) -> str:
    return value


def deserialize_json(data: str) -> DolbyVisionCompatibility:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DolbyVisionCompatibility value: {data!r}")
    return cast(DolbyVisionCompatibility, data)
