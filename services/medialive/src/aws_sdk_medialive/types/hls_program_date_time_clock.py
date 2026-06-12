"""Generated from Smithy shape ``com.amazonaws.medialive#HlsProgramDateTimeClock``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Program Date Time Clock"""
HlsProgramDateTimeClock: TypeAlias = Literal[
    "INITIALIZE_FROM_OUTPUT_TIMECODE",
    "SYSTEM_CLOCK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIALIZE_FROM_OUTPUT_TIMECODE",
        "SYSTEM_CLOCK",
    )
)


def serialize_json(value: HlsProgramDateTimeClock) -> str:
    return value


def deserialize_json(data: str) -> HlsProgramDateTimeClock:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsProgramDateTimeClock value: {data!r}")
    return cast(HlsProgramDateTimeClock, data)
