"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#LocalTimeZoneDetection``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.local_time_zone_detection_type

LocalTimeZoneDetection: TypeAlias = list[
    "aws_sdk_connectcampaignsv2.types.local_time_zone_detection_type.LocalTimeZoneDetectionType"
]


# --- restJson1 ser/de ---
def serialize_json(value: LocalTimeZoneDetection) -> list:
    return list(value)


def deserialize_json(data: list) -> LocalTimeZoneDetection:
    return list(data)
