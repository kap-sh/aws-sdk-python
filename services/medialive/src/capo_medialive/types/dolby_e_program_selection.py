"""Generated from Smithy shape ``com.amazonaws.medialive#DolbyEProgramSelection``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: DolbyEProgramSelection) -> str:
    return value


def deserialize_json(data: str) -> DolbyEProgramSelection:
    return cast(DolbyEProgramSelection, data)
