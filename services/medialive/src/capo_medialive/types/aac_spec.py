"""Generated from Smithy shape ``com.amazonaws.medialive#AacSpec``."""

from typing import Literal, TypeAlias, cast

"""Aac Spec"""
AacSpec: TypeAlias = Literal[
    "MPEG2",
    "MPEG4",
]


# --- restJson1 ser/de ---
def serialize_json(value: AacSpec) -> str:
    return value


def deserialize_json(data: str) -> AacSpec:
    return cast(AacSpec, data)
