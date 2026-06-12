"""Generated from Smithy shape ``com.amazonaws.medialive#Av1SceneChangeDetect``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Av1 Scene Change Detect"""
Av1SceneChangeDetect: TypeAlias = Literal[
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


def serialize_json(value: Av1SceneChangeDetect) -> str:
    return value


def deserialize_json(data: str) -> Av1SceneChangeDetect:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Av1SceneChangeDetect value: {data!r}")
    return cast(Av1SceneChangeDetect, data)
