"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsAudioBufferModel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Selects between the DVB and ATSC buffer models for Dolby Digital audio."""
M2tsAudioBufferModel: TypeAlias = Literal[
    "DVB",
    "ATSC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DVB",
        "ATSC",
    )
)


def serialize_json(value: M2tsAudioBufferModel) -> str:
    return value


def deserialize_json(data: str) -> M2tsAudioBufferModel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsAudioBufferModel value: {data!r}")
    return cast(M2tsAudioBufferModel, data)
