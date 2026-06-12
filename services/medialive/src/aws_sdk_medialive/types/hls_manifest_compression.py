"""Generated from Smithy shape ``com.amazonaws.medialive#HlsManifestCompression``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Manifest Compression"""
HlsManifestCompression: TypeAlias = Literal[
    "GZIP",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GZIP",
        "NONE",
    )
)


def serialize_json(value: HlsManifestCompression) -> str:
    return value


def deserialize_json(data: str) -> HlsManifestCompression:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsManifestCompression value: {data!r}")
    return cast(HlsManifestCompression, data)
