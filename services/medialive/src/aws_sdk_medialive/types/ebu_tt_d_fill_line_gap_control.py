"""Generated from Smithy shape ``com.amazonaws.medialive#EbuTtDFillLineGapControl``."""

from typing import Literal, TypeAlias, cast

"""Ebu Tt DFill Line Gap Control"""
EbuTtDFillLineGapControl: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EbuTtDFillLineGapControl) -> str:
    return value


def deserialize_json(data: str) -> EbuTtDFillLineGapControl:
    return cast(EbuTtDFillLineGapControl, data)
