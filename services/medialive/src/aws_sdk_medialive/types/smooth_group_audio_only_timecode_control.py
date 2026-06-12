"""Generated from Smithy shape ``com.amazonaws.medialive#SmoothGroupAudioOnlyTimecodeControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Smooth Group Audio Only Timecode Control"""
SmoothGroupAudioOnlyTimecodeControl: TypeAlias = Literal[
    "PASSTHROUGH",
    "USE_CONFIGURED_CLOCK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSTHROUGH",
        "USE_CONFIGURED_CLOCK",
    )
)


def serialize_json(value: SmoothGroupAudioOnlyTimecodeControl) -> str:
    return value


def deserialize_json(data: str) -> SmoothGroupAudioOnlyTimecodeControl:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SmoothGroupAudioOnlyTimecodeControl value: {data!r}"
        )
    return cast(SmoothGroupAudioOnlyTimecodeControl, data)
