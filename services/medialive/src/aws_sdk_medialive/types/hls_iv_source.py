"""Generated from Smithy shape ``com.amazonaws.medialive#HlsIvSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Iv Source"""
HlsIvSource: TypeAlias = Literal[
    "EXPLICIT",
    "FOLLOWS_SEGMENT_NUMBER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXPLICIT",
        "FOLLOWS_SEGMENT_NUMBER",
    )
)


def serialize_json(value: HlsIvSource) -> str:
    return value


def deserialize_json(data: str) -> HlsIvSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsIvSource value: {data!r}")
    return cast(HlsIvSource, data)
