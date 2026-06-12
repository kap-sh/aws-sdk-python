"""Generated from Smithy shape ``com.amazonaws.medialive#HlsClientCache``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Client Cache"""
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
