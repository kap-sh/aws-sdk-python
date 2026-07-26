"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3AtmosDynamicRangeCompressionRf``."""

from typing import Literal, TypeAlias, cast

"""Choose the Dolby dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby stream for the RF operating mode. Default value: Film light Related setting: To have MediaConvert use the value you specify here, keep the default value, Custom for the setting Dynamic range control. Otherwise, MediaConvert ignores Dynamic range compression RF. For information about the Dolby DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf."""
Eac3AtmosDynamicRangeCompressionRf: TypeAlias = Literal[
    "NONE",
    "FILM_STANDARD",
    "FILM_LIGHT",
    "MUSIC_STANDARD",
    "MUSIC_LIGHT",
    "SPEECH",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3AtmosDynamicRangeCompressionRf) -> str:
    return value


def deserialize_json(data: str) -> Eac3AtmosDynamicRangeCompressionRf:
    return cast(Eac3AtmosDynamicRangeCompressionRf, data)
