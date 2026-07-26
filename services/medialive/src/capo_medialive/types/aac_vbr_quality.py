"""Generated from Smithy shape ``com.amazonaws.medialive#AacVbrQuality``."""

from typing import Literal, TypeAlias, cast

"""Aac Vbr Quality"""
AacVbrQuality: TypeAlias = Literal[
    "HIGH",
    "LOW",
    "MEDIUM_HIGH",
    "MEDIUM_LOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: AacVbrQuality) -> str:
    return value


def deserialize_json(data: str) -> AacVbrQuality:
    return cast(AacVbrQuality, data)
