"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafStreamInfResolution``."""

from typing import Literal, TypeAlias, cast

"""Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest."""
CmafStreamInfResolution: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafStreamInfResolution) -> str:
    return value


def deserialize_json(data: str) -> CmafStreamInfResolution:
    return cast(CmafStreamInfResolution, data)
