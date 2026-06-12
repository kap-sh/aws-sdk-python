"""Generated from Smithy shape ``com.amazonaws.medialive#TimecodeConfigSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Timecode Config Source"""
TimecodeConfigSource: TypeAlias = Literal[
    "EMBEDDED",
    "SYSTEMCLOCK",
    "ZEROBASED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EMBEDDED",
        "SYSTEMCLOCK",
        "ZEROBASED",
    )
)


def serialize_json(value: TimecodeConfigSource) -> str:
    return value


def deserialize_json(data: str) -> TimecodeConfigSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimecodeConfigSource value: {data!r}")
    return cast(TimecodeConfigSource, data)
