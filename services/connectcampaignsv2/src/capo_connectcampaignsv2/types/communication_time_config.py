"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CommunicationTimeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.local_time_zone_config
    import capo_connectcampaignsv2.types.time_window


class CommunicationTimeConfig(TypedDict, closed=True):
    local_time_zone_config: (
        "capo_connectcampaignsv2.types.local_time_zone_config.LocalTimeZoneConfig"
    )
    telephony: NotRequired["capo_connectcampaignsv2.types.time_window.TimeWindow"]
    sms: NotRequired["capo_connectcampaignsv2.types.time_window.TimeWindow"]
    email: NotRequired["capo_connectcampaignsv2.types.time_window.TimeWindow"]
    whats_app: NotRequired["capo_connectcampaignsv2.types.time_window.TimeWindow"]


# --- restJson1 ser/de ---
def serialize_json(value: CommunicationTimeConfig) -> dict:
    out: dict = {}
    import capo_connectcampaignsv2.types.local_time_zone_config

    out["localTimeZoneConfig"] = (
        capo_connectcampaignsv2.types.local_time_zone_config.serialize_json(
            value["local_time_zone_config"]
        )
    )
    if "telephony" in value:
        import capo_connectcampaignsv2.types.time_window

        out["telephony"] = capo_connectcampaignsv2.types.time_window.serialize_json(
            value["telephony"]
        )
    if "sms" in value:
        import capo_connectcampaignsv2.types.time_window

        out["sms"] = capo_connectcampaignsv2.types.time_window.serialize_json(
            value["sms"]
        )
    if "email" in value:
        import capo_connectcampaignsv2.types.time_window

        out["email"] = capo_connectcampaignsv2.types.time_window.serialize_json(
            value["email"]
        )
    if "whats_app" in value:
        import capo_connectcampaignsv2.types.time_window

        out["whatsApp"] = capo_connectcampaignsv2.types.time_window.serialize_json(
            value["whats_app"]
        )
    return out


def deserialize_json(data: dict) -> CommunicationTimeConfig:
    out: CommunicationTimeConfig = {}  # type: ignore[typeddict-item]
    if "localTimeZoneConfig" in data:
        import capo_connectcampaignsv2.types.local_time_zone_config

        out["local_time_zone_config"] = (
            capo_connectcampaignsv2.types.local_time_zone_config.deserialize_json(
                data["localTimeZoneConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CommunicationTimeConfig.local_time_zone_config required"
        )
    if "telephony" in data:
        import capo_connectcampaignsv2.types.time_window

        out["telephony"] = capo_connectcampaignsv2.types.time_window.deserialize_json(
            data["telephony"]
        )
    if "sms" in data:
        import capo_connectcampaignsv2.types.time_window

        out["sms"] = capo_connectcampaignsv2.types.time_window.deserialize_json(
            data["sms"]
        )
    if "email" in data:
        import capo_connectcampaignsv2.types.time_window

        out["email"] = capo_connectcampaignsv2.types.time_window.deserialize_json(
            data["email"]
        )
    if "whatsApp" in data:
        import capo_connectcampaignsv2.types.time_window

        out["whats_app"] = capo_connectcampaignsv2.types.time_window.deserialize_json(
            data["whatsApp"]
        )
    return out
