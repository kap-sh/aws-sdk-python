"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#AudioMuxType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

AudioMuxType: TypeAlias = Literal[
    "AudioOnly",
    "AudioWithActiveSpeakerVideo",
    "AudioWithCompositedVideo",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AudioOnly",
        "AudioWithActiveSpeakerVideo",
        "AudioWithCompositedVideo",
    )
)


def serialize_json(value: AudioMuxType) -> str:
    return value


def deserialize_json(data: str) -> AudioMuxType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AudioMuxType value: {data!r}")
    return cast(AudioMuxType, data)
