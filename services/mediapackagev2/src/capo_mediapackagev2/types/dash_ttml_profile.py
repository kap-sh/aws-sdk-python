"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashTtmlProfile``."""

from typing import Literal, TypeAlias, cast

DashTtmlProfile: TypeAlias = Literal[
    "IMSC_1",
    "EBU_TT_D_101",
]


# --- restJson1 ser/de ---
def serialize_json(value: DashTtmlProfile) -> str:
    return value


def deserialize_json(data: str) -> DashTtmlProfile:
    return cast(DashTtmlProfile, data)
