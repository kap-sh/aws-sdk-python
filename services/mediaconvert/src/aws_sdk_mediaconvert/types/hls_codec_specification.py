"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsCodecSpecification``."""

from typing import Literal, TypeAlias, cast

"""Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation."""
HlsCodecSpecification: TypeAlias = Literal[
    "RFC_6381",
    "RFC_4281",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsCodecSpecification) -> str:
    return value


def deserialize_json(data: str) -> HlsCodecSpecification:
    return cast(HlsCodecSpecification, data)
