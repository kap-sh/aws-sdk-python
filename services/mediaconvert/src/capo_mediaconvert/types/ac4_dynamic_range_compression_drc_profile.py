"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Ac4DynamicRangeCompressionDrcProfile``."""

from typing import Literal, TypeAlias, cast

"""Choose the Dolby AC-4 dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby AC-4 stream for the specified decoder mode. For information about the Dolby AC-4 DRC profiles, see the Dolby AC-4 specification."""
Ac4DynamicRangeCompressionDrcProfile: TypeAlias = Literal[
    "NONE",
    "FILM_STANDARD",
    "FILM_LIGHT",
    "MUSIC_STANDARD",
    "MUSIC_LIGHT",
    "SPEECH",
]


# --- restJson1 ser/de ---
def serialize_json(value: Ac4DynamicRangeCompressionDrcProfile) -> str:
    return value


def deserialize_json(data: str) -> Ac4DynamicRangeCompressionDrcProfile:
    return cast(Ac4DynamicRangeCompressionDrcProfile, data)
