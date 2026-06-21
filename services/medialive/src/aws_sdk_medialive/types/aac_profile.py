"""Generated from Smithy shape ``com.amazonaws.medialive#AacProfile``."""

from typing import Literal, TypeAlias, cast

"""Aac Profile"""
AacProfile: TypeAlias = Literal[
    "HEV1",
    "HEV2",
    "LC",
]


# --- restJson1 ser/de ---
def serialize_json(value: AacProfile) -> str:
    return value


def deserialize_json(data: str) -> AacProfile:
    return cast(AacProfile, data)
