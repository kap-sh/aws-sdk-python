"""Generated from Smithy shape ``com.amazonaws.medialive#Mpeg2ScanType``."""

from typing import Literal, TypeAlias, cast

"""Mpeg2 Scan Type"""
Mpeg2ScanType: TypeAlias = Literal[
    "INTERLACED",
    "PROGRESSIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2ScanType) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2ScanType:
    return cast(Mpeg2ScanType, data)
