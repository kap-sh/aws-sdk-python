"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3AtmosDynamicRangeCompressionLine``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Choose the Dolby dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby stream for the line operating mode. Default value: Film light Related setting: To have MediaConvert use the value you specify here, keep the default value, Custom for the setting Dynamic range control. Otherwise, MediaConvert ignores Dynamic range compression line. For information about the Dolby DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf."""
Eac3AtmosDynamicRangeCompressionLine: TypeAlias = Literal[
    "NONE",
    "FILM_STANDARD",
    "FILM_LIGHT",
    "MUSIC_STANDARD",
    "MUSIC_LIGHT",
    "SPEECH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "FILM_STANDARD",
        "FILM_LIGHT",
        "MUSIC_STANDARD",
        "MUSIC_LIGHT",
        "SPEECH",
    )
)


def serialize_json(value: Eac3AtmosDynamicRangeCompressionLine) -> str:
    return value


def deserialize_json(data: str) -> Eac3AtmosDynamicRangeCompressionLine:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown Eac3AtmosDynamicRangeCompressionLine value: {data!r}"
        )
    return cast(Eac3AtmosDynamicRangeCompressionLine, data)
