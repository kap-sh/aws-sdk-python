"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashPeriodTrigger``."""

from typing import Literal, TypeAlias, cast

DashPeriodTrigger: TypeAlias = Literal[
    "AVAILS",
    "DRM_KEY_ROTATION",
    "SOURCE_CHANGES",
    "SOURCE_DISRUPTIONS",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DashPeriodTrigger) -> str:
    return value


def deserialize_json(data: str) -> DashPeriodTrigger:
    return cast(DashPeriodTrigger, data)
