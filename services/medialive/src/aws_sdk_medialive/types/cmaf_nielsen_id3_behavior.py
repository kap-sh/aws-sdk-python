"""Generated from Smithy shape ``com.amazonaws.medialive#CmafNielsenId3Behavior``."""

from typing import Literal, TypeAlias, cast

"""Cmaf Nielsen Id3 Behavior"""
CmafNielsenId3Behavior: TypeAlias = Literal[
    "NO_PASSTHROUGH",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafNielsenId3Behavior) -> str:
    return value


def deserialize_json(data: str) -> CmafNielsenId3Behavior:
    return cast(CmafNielsenId3Behavior, data)
