"""Generated from Smithy shape ``com.amazonaws.medialive#HlsCodecSpecification``."""

from typing import Literal, TypeAlias, cast

"""Hls Codec Specification"""
HlsCodecSpecification: TypeAlias = Literal[
    "RFC_4281",
    "RFC_6381",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsCodecSpecification) -> str:
    return value


def deserialize_json(data: str) -> HlsCodecSpecification:
    return cast(HlsCodecSpecification, data)
