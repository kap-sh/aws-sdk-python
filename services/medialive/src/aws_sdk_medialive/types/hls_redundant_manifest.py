"""Generated from Smithy shape ``com.amazonaws.medialive#HlsRedundantManifest``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Redundant Manifest"""
HlsRedundantManifest: TypeAlias = Literal[
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


def serialize_json(value: HlsRedundantManifest) -> str:
    return value


def deserialize_json(data: str) -> HlsRedundantManifest:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsRedundantManifest value: {data!r}")
    return cast(HlsRedundantManifest, data)
