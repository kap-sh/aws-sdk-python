"""Generated from Smithy shape ``com.amazonaws.medialive#HlsIvInManifest``."""

from typing import Literal, TypeAlias, cast

"""Hls Iv In Manifest"""
HlsIvInManifest: TypeAlias = Literal[
    "EXCLUDE",
    "INCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsIvInManifest) -> str:
    return value


def deserialize_json(data: str) -> HlsIvInManifest:
    return cast(HlsIvInManifest, data)
