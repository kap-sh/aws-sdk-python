"""Generated from Smithy shape ``com.amazonaws.medialive#HlsCaptionLanguageSetting``."""

from typing import Literal, TypeAlias, cast

"""Hls Caption Language Setting"""
HlsCaptionLanguageSetting: TypeAlias = Literal[
    "INSERT",
    "NONE",
    "OMIT",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsCaptionLanguageSetting) -> str:
    return value


def deserialize_json(data: str) -> HlsCaptionLanguageSetting:
    return cast(HlsCaptionLanguageSetting, data)
