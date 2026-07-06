"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#LocalTimeZoneConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.local_time_zone_detection
    import aws_sdk_connectcampaignsv2.types.local_time_zone_detection_scope
    import aws_sdk_connectcampaignsv2.types.time_zone


class LocalTimeZoneConfig(TypedDict, closed=True):
    default_time_zone: NotRequired[
        "aws_sdk_connectcampaignsv2.types.time_zone.TimeZone"
    ]
    local_time_zone_detection: NotRequired[
        "aws_sdk_connectcampaignsv2.types.local_time_zone_detection.LocalTimeZoneDetection"
    ]
    local_time_zone_detection_scope: NotRequired[
        "aws_sdk_connectcampaignsv2.types.local_time_zone_detection_scope.LocalTimeZoneDetectionScope"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: LocalTimeZoneConfig) -> dict:
    out: dict = {}
    if "default_time_zone" in value:
        out["defaultTimeZone"] = value["default_time_zone"]
    if "local_time_zone_detection" in value:
        import aws_sdk_connectcampaignsv2.types.local_time_zone_detection

        out["localTimeZoneDetection"] = (
            aws_sdk_connectcampaignsv2.types.local_time_zone_detection.serialize_json(
                value["local_time_zone_detection"]
            )
        )
    if "local_time_zone_detection_scope" in value:
        out["localTimeZoneDetectionScope"] = value["local_time_zone_detection_scope"]
    return out


def deserialize_json(data: dict) -> LocalTimeZoneConfig:
    out: LocalTimeZoneConfig = {}  # type: ignore[typeddict-item]
    if "defaultTimeZone" in data:
        out["default_time_zone"] = data["defaultTimeZone"]
    if "localTimeZoneDetection" in data:
        import aws_sdk_connectcampaignsv2.types.local_time_zone_detection

        out["local_time_zone_detection"] = (
            aws_sdk_connectcampaignsv2.types.local_time_zone_detection.deserialize_json(
                data["localTimeZoneDetection"]
            )
        )
    if "localTimeZoneDetectionScope" in data:
        out["local_time_zone_detection_scope"] = data["localTimeZoneDetectionScope"]
    return out
