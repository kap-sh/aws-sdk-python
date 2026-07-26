"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#AudioMuxType``."""

from typing import Literal, TypeAlias, cast

AudioMuxType: TypeAlias = Literal[
    "AudioOnly",
    "AudioWithActiveSpeakerVideo",
    "AudioWithCompositedVideo",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioMuxType) -> str:
    return value


def deserialize_json(data: str) -> AudioMuxType:
    return cast(AudioMuxType, data)
