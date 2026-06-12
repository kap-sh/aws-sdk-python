"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3DynamicRangeCompressionRf``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the RF operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf."""
Eac3DynamicRangeCompressionRf: TypeAlias = Literal[
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


def serialize_json(value: Eac3DynamicRangeCompressionRf) -> str:
    return value


def deserialize_json(data: str) -> Eac3DynamicRangeCompressionRf:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown Eac3DynamicRangeCompressionRf value: {data!r}"
        )
    return cast(Eac3DynamicRangeCompressionRf, data)
