"""Generated from Smithy shape ``com.amazonaws.medialive#FecOutputIncludeFec``."""

from typing import Literal, TypeAlias, cast

"""Fec Output Include Fec"""
FecOutputIncludeFec: TypeAlias = Literal[
    "COLUMN",
    "COLUMN_AND_ROW",
]


# --- restJson1 ser/de ---
def serialize_json(value: FecOutputIncludeFec) -> str:
    return value


def deserialize_json(data: str) -> FecOutputIncludeFec:
    return cast(FecOutputIncludeFec, data)
