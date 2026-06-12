"""Generated from Smithy shape ``com.amazonaws.medialive#HlsProgramDateTime``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Program Date Time"""
HlsProgramDateTime: TypeAlias = Literal[
    "EXCLUDE",
    "INCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXCLUDE",
        "INCLUDE",
    )
)


def serialize_json(value: HlsProgramDateTime) -> str:
    return value


def deserialize_json(data: str) -> HlsProgramDateTime:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsProgramDateTime value: {data!r}")
    return cast(HlsProgramDateTime, data)
