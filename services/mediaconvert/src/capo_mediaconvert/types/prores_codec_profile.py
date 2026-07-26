"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ProresCodecProfile``."""

from typing import Literal, TypeAlias, cast

"""Use Profile to specify the type of Apple ProRes codec to use for this output."""
ProresCodecProfile: TypeAlias = Literal[
    "APPLE_PRORES_422",
    "APPLE_PRORES_422_HQ",
    "APPLE_PRORES_422_LT",
    "APPLE_PRORES_422_PROXY",
    "APPLE_PRORES_4444",
    "APPLE_PRORES_4444_XQ",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProresCodecProfile) -> str:
    return value


def deserialize_json(data: str) -> ProresCodecProfile:
    return cast(ProresCodecProfile, data)
