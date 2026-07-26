"""Generated from Smithy shape ``com.amazonaws.medialive#Smpte2038DataPreference``."""

from typing import Literal, TypeAlias, cast

"""Smpte2038 Data Preference"""
Smpte2038DataPreference: TypeAlias = Literal[
    "IGNORE",
    "PREFER",
]


# --- restJson1 ser/de ---
def serialize_json(value: Smpte2038DataPreference) -> str:
    return value


def deserialize_json(data: str) -> Smpte2038DataPreference:
    return cast(Smpte2038DataPreference, data)
