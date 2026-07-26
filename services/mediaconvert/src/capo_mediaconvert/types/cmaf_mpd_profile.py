"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafMpdProfile``."""

from typing import Literal, TypeAlias, cast

"""Specify whether your DASH profile is on-demand or main. When you choose Main profile, the service signals urn:mpeg:dash:profile:isoff-main:2011 in your .mpd DASH manifest. When you choose On-demand, the service signals urn:mpeg:dash:profile:isoff-on-demand:2011 in your .mpd. When you choose On-demand, you must also set the output group setting Segment control to Single file."""
CmafMpdProfile: TypeAlias = Literal[
    "MAIN_PROFILE",
    "ON_DEMAND_PROFILE",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafMpdProfile) -> str:
    return value


def deserialize_json(data: str) -> CmafMpdProfile:
    return cast(CmafMpdProfile, data)
