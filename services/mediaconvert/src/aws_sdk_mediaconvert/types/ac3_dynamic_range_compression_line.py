"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Ac3DynamicRangeCompressionLine``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the line operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf."""
Ac3DynamicRangeCompressionLine: TypeAlias = Literal[
    "FILM_STANDARD",
    "FILM_LIGHT",
    "MUSIC_STANDARD",
    "MUSIC_LIGHT",
    "SPEECH",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FILM_STANDARD",
        "FILM_LIGHT",
        "MUSIC_STANDARD",
        "MUSIC_LIGHT",
        "SPEECH",
        "NONE",
    )
)


def serialize_json(value: Ac3DynamicRangeCompressionLine) -> str:
    return value


def deserialize_json(data: str) -> Ac3DynamicRangeCompressionLine:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown Ac3DynamicRangeCompressionLine value: {data!r}"
        )
    return cast(Ac3DynamicRangeCompressionLine, data)
