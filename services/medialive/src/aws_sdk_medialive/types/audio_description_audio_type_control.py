"""Generated from Smithy shape ``com.amazonaws.medialive#AudioDescriptionAudioTypeControl``."""

from typing import Literal, TypeAlias, cast

"""Audio Description Audio Type Control"""
AudioDescriptionAudioTypeControl: TypeAlias = Literal[
    "FOLLOW_INPUT",
    "USE_CONFIGURED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioDescriptionAudioTypeControl) -> str:
    return value


def deserialize_json(data: str) -> AudioDescriptionAudioTypeControl:
    return cast(AudioDescriptionAudioTypeControl, data)
