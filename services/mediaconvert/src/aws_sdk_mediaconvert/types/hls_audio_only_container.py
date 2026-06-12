"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsAudioOnlyContainer``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Use this setting only in audio-only outputs. Choose MPEG-2 Transport Stream (M2TS) to create a file in an MPEG2-TS container. Keep the default value Automatic to create a raw audio-only file with no container. Regardless of the value that you specify here, if this output has video, the service will place outputs into an MPEG2-TS container."""
HlsAudioOnlyContainer: TypeAlias = Literal[
    "AUTOMATIC",
    "M2TS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "M2TS",
    )
)


def serialize_json(value: HlsAudioOnlyContainer) -> str:
    return value


def deserialize_json(data: str) -> HlsAudioOnlyContainer:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsAudioOnlyContainer value: {data!r}")
    return cast(HlsAudioOnlyContainer, data)
