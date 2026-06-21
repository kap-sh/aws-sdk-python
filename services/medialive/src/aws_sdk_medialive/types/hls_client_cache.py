"""Generated from Smithy shape ``com.amazonaws.medialive#HlsClientCache``."""

from typing import Literal, TypeAlias, cast

"""Hls Client Cache"""
HlsClientCache: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsClientCache) -> str:
    return value


def deserialize_json(data: str) -> HlsClientCache:
    return cast(HlsClientCache, data)
