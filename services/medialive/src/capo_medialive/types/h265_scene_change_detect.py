"""Generated from Smithy shape ``com.amazonaws.medialive#H265SceneChangeDetect``."""

from typing import Literal, TypeAlias, cast

"""H265 Scene Change Detect"""
H265SceneChangeDetect: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265SceneChangeDetect) -> str:
    return value


def deserialize_json(data: str) -> H265SceneChangeDetect:
    return cast(H265SceneChangeDetect, data)
