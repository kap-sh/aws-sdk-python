"""Generated from Smithy shape ``com.amazonaws.medialive#HlsScte35SourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Scte35 Source Type"""
HlsScte35SourceType: TypeAlias = Literal[
    "MANIFEST",
    "SEGMENTS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MANIFEST",
        "SEGMENTS",
    )
)


def serialize_json(value: HlsScte35SourceType) -> str:
    return value


def deserialize_json(data: str) -> HlsScte35SourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsScte35SourceType value: {data!r}")
    return cast(HlsScte35SourceType, data)
