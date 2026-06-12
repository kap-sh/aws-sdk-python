"""Generated from Smithy shape ``com.amazonaws.medialive#HlsIvInManifest``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Iv In Manifest"""
HlsIvInManifest: TypeAlias = Literal[
    "EXCLUDE",
    "INCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXCLUDE",
        "INCLUDE",
    )
)


def serialize_json(value: HlsIvInManifest) -> str:
    return value


def deserialize_json(data: str) -> HlsIvInManifest:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsIvInManifest value: {data!r}")
    return cast(HlsIvInManifest, data)
