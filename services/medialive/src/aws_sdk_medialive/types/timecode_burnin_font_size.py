"""Generated from Smithy shape ``com.amazonaws.medialive#TimecodeBurninFontSize``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Timecode Burnin Font Size"""
TimecodeBurninFontSize: TypeAlias = Literal[
    "EXTRA_SMALL_10",
    "LARGE_48",
    "MEDIUM_32",
    "SMALL_16",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXTRA_SMALL_10",
        "LARGE_48",
        "MEDIUM_32",
        "SMALL_16",
    )
)


def serialize_json(value: TimecodeBurninFontSize) -> str:
    return value


def deserialize_json(data: str) -> TimecodeBurninFontSize:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimecodeBurninFontSize value: {data!r}")
    return cast(TimecodeBurninFontSize, data)
