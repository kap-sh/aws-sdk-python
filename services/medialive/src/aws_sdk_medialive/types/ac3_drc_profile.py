"""Generated from Smithy shape ``com.amazonaws.medialive#Ac3DrcProfile``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Ac3 Drc Profile"""
Ac3DrcProfile: TypeAlias = Literal[
    "FILM_STANDARD",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FILM_STANDARD",
        "NONE",
    )
)


def serialize_json(value: Ac3DrcProfile) -> str:
    return value


def deserialize_json(data: str) -> Ac3DrcProfile:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Ac3DrcProfile value: {data!r}")
    return cast(Ac3DrcProfile, data)
