"""Generated from Smithy shape ``com.amazonaws.medialive#HlsRedundantManifest``."""

from typing import Literal, TypeAlias, cast

"""Hls Redundant Manifest"""
HlsRedundantManifest: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsRedundantManifest) -> str:
    return value


def deserialize_json(data: str) -> HlsRedundantManifest:
    return cast(HlsRedundantManifest, data)
