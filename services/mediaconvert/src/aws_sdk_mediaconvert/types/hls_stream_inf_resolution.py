"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsStreamInfResolution``."""

from typing import Literal, TypeAlias, cast

"""Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest."""
HlsStreamInfResolution: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsStreamInfResolution) -> str:
    return value


def deserialize_json(data: str) -> HlsStreamInfResolution:
    return cast(HlsStreamInfResolution, data)
