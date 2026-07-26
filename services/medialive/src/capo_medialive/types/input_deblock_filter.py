"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeblockFilter``."""

from typing import Literal, TypeAlias, cast

"""Input Deblock Filter"""
InputDeblockFilter: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputDeblockFilter) -> str:
    return value


def deserialize_json(data: str) -> InputDeblockFilter:
    return cast(InputDeblockFilter, data)
