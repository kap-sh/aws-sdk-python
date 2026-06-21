"""Generated from Smithy shape ``com.amazonaws.medialive#CmafId3Behavior``."""

from typing import Literal, TypeAlias, cast

"""Cmaf Id3 Behavior"""
CmafId3Behavior: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafId3Behavior) -> str:
    return value


def deserialize_json(data: str) -> CmafId3Behavior:
    return cast(CmafId3Behavior, data)
