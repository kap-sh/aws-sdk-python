"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashProfile``."""

from typing import Literal, TypeAlias, cast

DashProfile: TypeAlias = Literal["DVB_DASH",]


# --- restJson1 ser/de ---
def serialize_json(value: DashProfile) -> str:
    return value


def deserialize_json(data: str) -> DashProfile:
    return cast(DashProfile, data)
