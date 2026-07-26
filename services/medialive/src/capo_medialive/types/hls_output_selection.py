"""Generated from Smithy shape ``com.amazonaws.medialive#HlsOutputSelection``."""

from typing import Literal, TypeAlias, cast

"""Hls Output Selection"""
HlsOutputSelection: TypeAlias = Literal[
    "MANIFESTS_AND_SEGMENTS",
    "SEGMENTS_ONLY",
    "VARIANT_MANIFESTS_AND_SEGMENTS",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsOutputSelection) -> str:
    return value


def deserialize_json(data: str) -> HlsOutputSelection:
    return cast(HlsOutputSelection, data)
