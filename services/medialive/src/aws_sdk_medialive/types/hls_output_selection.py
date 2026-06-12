"""Generated from Smithy shape ``com.amazonaws.medialive#HlsOutputSelection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Output Selection"""
HlsOutputSelection: TypeAlias = Literal[
    "MANIFESTS_AND_SEGMENTS",
    "SEGMENTS_ONLY",
    "VARIANT_MANIFESTS_AND_SEGMENTS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MANIFESTS_AND_SEGMENTS",
        "SEGMENTS_ONLY",
        "VARIANT_MANIFESTS_AND_SEGMENTS",
    )
)


def serialize_json(value: HlsOutputSelection) -> str:
    return value


def deserialize_json(data: str) -> HlsOutputSelection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsOutputSelection value: {data!r}")
    return cast(HlsOutputSelection, data)
