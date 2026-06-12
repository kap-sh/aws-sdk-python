"""Generated from Smithy shape ``com.amazonaws.medialive#Smpte2038DataPreference``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Smpte2038 Data Preference"""
Smpte2038DataPreference: TypeAlias = Literal[
    "IGNORE",
    "PREFER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IGNORE",
        "PREFER",
    )
)


def serialize_json(value: Smpte2038DataPreference) -> str:
    return value


def deserialize_json(data: str) -> Smpte2038DataPreference:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Smpte2038DataPreference value: {data!r}")
    return cast(Smpte2038DataPreference, data)
