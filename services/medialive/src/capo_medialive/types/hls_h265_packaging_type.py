"""Generated from Smithy shape ``com.amazonaws.medialive#HlsH265PackagingType``."""

from typing import Literal, TypeAlias, cast

"""Hls H265 Packaging Type"""
HlsH265PackagingType: TypeAlias = Literal[
    "HEV1",
    "HVC1",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsH265PackagingType) -> str:
    return value


def deserialize_json(data: str) -> HlsH265PackagingType:
    return cast(HlsH265PackagingType, data)
