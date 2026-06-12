"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CommunicationTimeConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.local_time_zone_config
    import aws_sdk_connectcampaignsv2.types.time_window


class CommunicationTimeConfig(TypedDict):
    local_time_zone_config: (
        "aws_sdk_connectcampaignsv2.types.local_time_zone_config.LocalTimeZoneConfig"
    )
    telephony: NotRequired["aws_sdk_connectcampaignsv2.types.time_window.TimeWindow"]
    sms: NotRequired["aws_sdk_connectcampaignsv2.types.time_window.TimeWindow"]
    email: NotRequired["aws_sdk_connectcampaignsv2.types.time_window.TimeWindow"]
    whats_app: NotRequired["aws_sdk_connectcampaignsv2.types.time_window.TimeWindow"]


# --- restJson1 ser/de ---
def serialize_json(value: CommunicationTimeConfig) -> dict:
    out: dict = {}
    import aws_sdk_connectcampaignsv2.types.local_time_zone_config

    out["localTimeZoneConfig"] = (
        aws_sdk_connectcampaignsv2.types.local_time_zone_config.serialize_json(
            value["local_time_zone_config"]
        )
    )
    if "telephony" in value:
        import aws_sdk_connectcampaignsv2.types.time_window

        out["telephony"] = aws_sdk_connectcampaignsv2.types.time_window.serialize_json(
            value["telephony"]
        )
    if "sms" in value:
        import aws_sdk_connectcampaignsv2.types.time_window

        out["sms"] = aws_sdk_connectcampaignsv2.types.time_window.serialize_json(
            value["sms"]
        )
    if "email" in value:
        import aws_sdk_connectcampaignsv2.types.time_window

        out["email"] = aws_sdk_connectcampaignsv2.types.time_window.serialize_json(
            value["email"]
        )
    if "whats_app" in value:
        import aws_sdk_connectcampaignsv2.types.time_window

        out["whatsApp"] = aws_sdk_connectcampaignsv2.types.time_window.serialize_json(
            value["whats_app"]
        )
    return out


def deserialize_json(data: dict) -> CommunicationTimeConfig:
    out: CommunicationTimeConfig = {}  # type: ignore[typeddict-item]
    if "localTimeZoneConfig" in data:
        import aws_sdk_connectcampaignsv2.types.local_time_zone_config

        out["local_time_zone_config"] = (
            aws_sdk_connectcampaignsv2.types.local_time_zone_config.deserialize_json(
                data["localTimeZoneConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CommunicationTimeConfig.local_time_zone_config required"
        )
    if "telephony" in data:
        import aws_sdk_connectcampaignsv2.types.time_window

        out["telephony"] = (
            aws_sdk_connectcampaignsv2.types.time_window.deserialize_json(
                data["telephony"]
            )
        )
    if "sms" in data:
        import aws_sdk_connectcampaignsv2.types.time_window

        out["sms"] = aws_sdk_connectcampaignsv2.types.time_window.deserialize_json(
            data["sms"]
        )
    if "email" in data:
        import aws_sdk_connectcampaignsv2.types.time_window

        out["email"] = aws_sdk_connectcampaignsv2.types.time_window.deserialize_json(
            data["email"]
        )
    if "whatsApp" in data:
        import aws_sdk_connectcampaignsv2.types.time_window

        out["whats_app"] = (
            aws_sdk_connectcampaignsv2.types.time_window.deserialize_json(
                data["whatsApp"]
            )
        )
    return out
