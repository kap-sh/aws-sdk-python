"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsClientCache``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Disable this setting only when your workflow requires the #EXT-X-ALLOW-CACHE:no tag. Otherwise, keep the default value Enabled and control caching in your video distribution set up. For example, use the Cache-Control http header."""
HlsClientCache: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: HlsClientCache) -> str:
    return value


def deserialize_json(data: str) -> HlsClientCache:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsClientCache value: {data!r}")
    return cast(HlsClientCache, data)
