"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsCodecSpecification``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation."""
HlsCodecSpecification: TypeAlias = Literal[
    "RFC_6381",
    "RFC_4281",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RFC_6381",
        "RFC_4281",
    )
)


def serialize_json(value: HlsCodecSpecification) -> str:
    return value


def deserialize_json(data: str) -> HlsCodecSpecification:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsCodecSpecification value: {data!r}")
    return cast(HlsCodecSpecification, data)
