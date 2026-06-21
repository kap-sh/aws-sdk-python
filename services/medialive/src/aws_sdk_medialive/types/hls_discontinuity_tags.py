"""Generated from Smithy shape ``com.amazonaws.medialive#HlsDiscontinuityTags``."""

from typing import Literal, TypeAlias, cast

"""Hls Discontinuity Tags"""
HlsDiscontinuityTags: TypeAlias = Literal[
    "INSERT",
    "NEVER_INSERT",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsDiscontinuityTags) -> str:
    return value


def deserialize_json(data: str) -> HlsDiscontinuityTags:
    return cast(HlsDiscontinuityTags, data)
