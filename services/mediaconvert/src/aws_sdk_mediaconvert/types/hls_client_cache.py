"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsClientCache``."""

from typing import Literal, TypeAlias, cast

"""Disable this setting only when your workflow requires the #EXT-X-ALLOW-CACHE:no tag. Otherwise, keep the default value Enabled and control caching in your video distribution set up. For example, use the Cache-Control http header."""
HlsClientCache: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsClientCache) -> str:
    return value


def deserialize_json(data: str) -> HlsClientCache:
    return cast(HlsClientCache, data)
