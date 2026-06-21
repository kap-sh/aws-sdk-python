"""Generated from Smithy shape ``com.amazonaws.medialive#HlsManifestCompression``."""

from typing import Literal, TypeAlias, cast

"""Hls Manifest Compression"""
HlsManifestCompression: TypeAlias = Literal[
    "GZIP",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsManifestCompression) -> str:
    return value


def deserialize_json(data: str) -> HlsManifestCompression:
    return cast(HlsManifestCompression, data)
