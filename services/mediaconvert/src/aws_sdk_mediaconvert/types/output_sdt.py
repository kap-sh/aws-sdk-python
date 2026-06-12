"""Generated from Smithy shape ``com.amazonaws.mediaconvert#OutputSdt``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Selects method of inserting SDT information into output stream. \"Follow input SDT\" copies SDT information from input stream to output stream. \"Follow input SDT if present\" copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. Enter \"SDT Manually\" means user will enter the SDT information. \"No SDT\" means output stream will not contain SDT information."""
OutputSdt: TypeAlias = Literal[
    "SDT_FOLLOW",
    "SDT_FOLLOW_IF_PRESENT",
    "SDT_MANUAL",
    "SDT_NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SDT_FOLLOW",
        "SDT_FOLLOW_IF_PRESENT",
        "SDT_MANUAL",
        "SDT_NONE",
    )
)


def serialize_json(value: OutputSdt) -> str:
    return value


def deserialize_json(data: str) -> OutputSdt:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutputSdt value: {data!r}")
    return cast(OutputSdt, data)
