"""Generated from Smithy shape ``com.amazonaws.medialive#InputDenoiseFilter``."""

from typing import Literal, TypeAlias, cast

"""Input Denoise Filter"""
InputDenoiseFilter: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputDenoiseFilter) -> str:
    return value


def deserialize_json(data: str) -> InputDenoiseFilter:
    return cast(InputDenoiseFilter, data)
