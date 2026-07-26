"""Generated from Smithy shape ``com.amazonaws.medialive#H264SceneChangeDetect``."""

from typing import Literal, TypeAlias, cast

"""H264 Scene Change Detect"""
H264SceneChangeDetect: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264SceneChangeDetect) -> str:
    return value


def deserialize_json(data: str) -> H264SceneChangeDetect:
    return cast(H264SceneChangeDetect, data)
