"""Generated from Smithy shape ``com.amazonaws.medialive#HlsDiscontinuityTags``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Discontinuity Tags"""
HlsDiscontinuityTags: TypeAlias = Literal[
    "INSERT",
    "NEVER_INSERT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSERT",
        "NEVER_INSERT",
    )
)


def serialize_json(value: HlsDiscontinuityTags) -> str:
    return value


def deserialize_json(data: str) -> HlsDiscontinuityTags:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsDiscontinuityTags value: {data!r}")
    return cast(HlsDiscontinuityTags, data)
