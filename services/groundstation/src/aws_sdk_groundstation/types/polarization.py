"""Generated from Smithy shape ``com.amazonaws.groundstation#Polarization``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

Polarization: TypeAlias = Literal[
    "RIGHT_HAND",
    "LEFT_HAND",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RIGHT_HAND",
        "LEFT_HAND",
        "NONE",
    )
)


def serialize_json(value: Polarization) -> str:
    return value


def deserialize_json(data: str) -> Polarization:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Polarization value: {data!r}")
    return cast(Polarization, data)
