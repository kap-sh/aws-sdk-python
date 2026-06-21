"""Generated from Smithy shape ``com.amazonaws.medialive#AudioOnlyHlsTrackType``."""

from typing import Literal, TypeAlias, cast

"""Audio Only Hls Track Type"""
AudioOnlyHlsTrackType: TypeAlias = Literal[
    "ALTERNATE_AUDIO_AUTO_SELECT",
    "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT",
    "ALTERNATE_AUDIO_NOT_AUTO_SELECT",
    "AUDIO_ONLY_VARIANT_STREAM",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioOnlyHlsTrackType) -> str:
    return value


def deserialize_json(data: str) -> AudioOnlyHlsTrackType:
    return cast(AudioOnlyHlsTrackType, data)
