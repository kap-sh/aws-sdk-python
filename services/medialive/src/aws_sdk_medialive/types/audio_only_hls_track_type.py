"""Generated from Smithy shape ``com.amazonaws.medialive#AudioOnlyHlsTrackType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Audio Only Hls Track Type"""
AudioOnlyHlsTrackType: TypeAlias = Literal[
    "ALTERNATE_AUDIO_AUTO_SELECT",
    "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT",
    "ALTERNATE_AUDIO_NOT_AUTO_SELECT",
    "AUDIO_ONLY_VARIANT_STREAM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALTERNATE_AUDIO_AUTO_SELECT",
        "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT",
        "ALTERNATE_AUDIO_NOT_AUTO_SELECT",
        "AUDIO_ONLY_VARIANT_STREAM",
    )
)


def serialize_json(value: AudioOnlyHlsTrackType) -> str:
    return value


def deserialize_json(data: str) -> AudioOnlyHlsTrackType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AudioOnlyHlsTrackType value: {data!r}")
    return cast(AudioOnlyHlsTrackType, data)
