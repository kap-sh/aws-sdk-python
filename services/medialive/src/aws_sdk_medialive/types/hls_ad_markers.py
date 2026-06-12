"""Generated from Smithy shape ``com.amazonaws.medialive#HlsAdMarkers``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Ad Markers"""
HlsAdMarkers: TypeAlias = Literal[
    "ADOBE",
    "ELEMENTAL",
    "ELEMENTAL_SCTE35",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADOBE",
        "ELEMENTAL",
        "ELEMENTAL_SCTE35",
    )
)


def serialize_json(value: HlsAdMarkers) -> str:
    return value


def deserialize_json(data: str) -> HlsAdMarkers:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsAdMarkers value: {data!r}")
    return cast(HlsAdMarkers, data)
