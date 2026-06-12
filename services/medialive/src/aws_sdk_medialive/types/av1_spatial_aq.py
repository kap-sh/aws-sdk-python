"""Generated from Smithy shape ``com.amazonaws.medialive#Av1SpatialAq``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Av1 Spatial Aq"""
Av1SpatialAq: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: Av1SpatialAq) -> str:
    return value


def deserialize_json(data: str) -> Av1SpatialAq:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Av1SpatialAq value: {data!r}")
    return cast(Av1SpatialAq, data)
