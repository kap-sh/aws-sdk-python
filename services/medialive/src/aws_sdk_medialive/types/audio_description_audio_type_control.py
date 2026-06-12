"""Generated from Smithy shape ``com.amazonaws.medialive#AudioDescriptionAudioTypeControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Audio Description Audio Type Control"""
AudioDescriptionAudioTypeControl: TypeAlias = Literal[
    "FOLLOW_INPUT",
    "USE_CONFIGURED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FOLLOW_INPUT",
        "USE_CONFIGURED",
    )
)


def serialize_json(value: AudioDescriptionAudioTypeControl) -> str:
    return value


def deserialize_json(data: str) -> AudioDescriptionAudioTypeControl:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AudioDescriptionAudioTypeControl value: {data!r}"
        )
    return cast(AudioDescriptionAudioTypeControl, data)
