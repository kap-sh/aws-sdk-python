"""Generated from Smithy shape ``com.amazonaws.medialive#HlsStreamInfResolution``."""

from typing import Literal, TypeAlias, cast

"""Hls Stream Inf Resolution"""
HlsStreamInfResolution: TypeAlias = Literal[
    "EXCLUDE",
    "INCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsStreamInfResolution) -> str:
    return value


def deserialize_json(data: str) -> HlsStreamInfResolution:
    return cast(HlsStreamInfResolution, data)
