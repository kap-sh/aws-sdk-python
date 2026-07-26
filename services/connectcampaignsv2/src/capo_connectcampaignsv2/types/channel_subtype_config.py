"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#ChannelSubtypeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.email_channel_subtype_config
    import capo_connectcampaignsv2.types.sms_channel_subtype_config
    import capo_connectcampaignsv2.types.telephony_channel_subtype_config
    import capo_connectcampaignsv2.types.whats_app_channel_subtype_config


class ChannelSubtypeConfig(TypedDict, closed=True):
    telephony: NotRequired[
        "capo_connectcampaignsv2.types.telephony_channel_subtype_config.TelephonyChannelSubtypeConfig"
    ]
    sms: NotRequired[
        "capo_connectcampaignsv2.types.sms_channel_subtype_config.SmsChannelSubtypeConfig"
    ]
    email: NotRequired[
        "capo_connectcampaignsv2.types.email_channel_subtype_config.EmailChannelSubtypeConfig"
    ]
    whats_app: NotRequired[
        "capo_connectcampaignsv2.types.whats_app_channel_subtype_config.WhatsAppChannelSubtypeConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelSubtypeConfig) -> dict:
    out: dict = {}
    if "telephony" in value:
        import capo_connectcampaignsv2.types.telephony_channel_subtype_config

        out["telephony"] = (
            capo_connectcampaignsv2.types.telephony_channel_subtype_config.serialize_json(
                value["telephony"]
            )
        )
    if "sms" in value:
        import capo_connectcampaignsv2.types.sms_channel_subtype_config

        out["sms"] = (
            capo_connectcampaignsv2.types.sms_channel_subtype_config.serialize_json(
                value["sms"]
            )
        )
    if "email" in value:
        import capo_connectcampaignsv2.types.email_channel_subtype_config

        out["email"] = (
            capo_connectcampaignsv2.types.email_channel_subtype_config.serialize_json(
                value["email"]
            )
        )
    if "whats_app" in value:
        import capo_connectcampaignsv2.types.whats_app_channel_subtype_config

        out["whatsApp"] = (
            capo_connectcampaignsv2.types.whats_app_channel_subtype_config.serialize_json(
                value["whats_app"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChannelSubtypeConfig:
    out: ChannelSubtypeConfig = {}  # type: ignore[typeddict-item]
    if "telephony" in data:
        import capo_connectcampaignsv2.types.telephony_channel_subtype_config

        out["telephony"] = (
            capo_connectcampaignsv2.types.telephony_channel_subtype_config.deserialize_json(
                data["telephony"]
            )
        )
    if "sms" in data:
        import capo_connectcampaignsv2.types.sms_channel_subtype_config

        out["sms"] = (
            capo_connectcampaignsv2.types.sms_channel_subtype_config.deserialize_json(
                data["sms"]
            )
        )
    if "email" in data:
        import capo_connectcampaignsv2.types.email_channel_subtype_config

        out["email"] = (
            capo_connectcampaignsv2.types.email_channel_subtype_config.deserialize_json(
                data["email"]
            )
        )
    if "whatsApp" in data:
        import capo_connectcampaignsv2.types.whats_app_channel_subtype_config

        out["whats_app"] = (
            capo_connectcampaignsv2.types.whats_app_channel_subtype_config.deserialize_json(
                data["whatsApp"]
            )
        )
    return out
