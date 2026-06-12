"""Generated from Smithy shape ``com.amazonaws.medialive#Ac3AttenuationControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Ac3 Attenuation Control"""
Ac3AttenuationControl: TypeAlias = Literal[
    "ATTENUATE_3_DB",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ATTENUATE_3_DB",
        "NONE",
    )
)


def serialize_json(value: Ac3AttenuationControl) -> str:
    return value


def deserialize_json(data: str) -> Ac3AttenuationControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Ac3AttenuationControl value: {data!r}")
    return cast(Ac3AttenuationControl, data)
