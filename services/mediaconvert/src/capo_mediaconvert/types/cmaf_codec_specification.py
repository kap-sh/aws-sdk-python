"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafCodecSpecification``."""

from typing import Literal, TypeAlias, cast

"""Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation."""
CmafCodecSpecification: TypeAlias = Literal[
    "RFC_6381",
    "RFC_4281",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafCodecSpecification) -> str:
    return value


def deserialize_json(data: str) -> CmafCodecSpecification:
    return cast(CmafCodecSpecification, data)
