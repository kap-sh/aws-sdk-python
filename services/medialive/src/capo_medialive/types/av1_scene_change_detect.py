"""Generated from Smithy shape ``com.amazonaws.medialive#Av1SceneChangeDetect``."""

from typing import Literal, TypeAlias, cast

"""Av1 Scene Change Detect"""
Av1SceneChangeDetect: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Av1SceneChangeDetect) -> str:
    return value


def deserialize_json(data: str) -> Av1SceneChangeDetect:
    return cast(Av1SceneChangeDetect, data)
