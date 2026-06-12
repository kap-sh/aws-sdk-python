"""Generated from Smithy shape ``com.amazonaws.medialive#DolbyEProgramSelection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Dolby EProgram Selection"""
DolbyEProgramSelection: TypeAlias = Literal[
    "ALL_CHANNELS",
    "PROGRAM_1",
    "PROGRAM_2",
    "PROGRAM_3",
    "PROGRAM_4",
    "PROGRAM_5",
    "PROGRAM_6",
    "PROGRAM_7",
    "PROGRAM_8",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_CHANNELS",
        "PROGRAM_1",
        "PROGRAM_2",
        "PROGRAM_3",
        "PROGRAM_4",
        "PROGRAM_5",
        "PROGRAM_6",
        "PROGRAM_7",
        "PROGRAM_8",
    )
)


def serialize_json(value: DolbyEProgramSelection) -> str:
    return value


def deserialize_json(data: str) -> DolbyEProgramSelection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DolbyEProgramSelection value: {data!r}")
    return cast(DolbyEProgramSelection, data)
