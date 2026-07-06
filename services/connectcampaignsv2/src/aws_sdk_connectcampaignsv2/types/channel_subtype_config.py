"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#ChannelSubtypeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.email_channel_subtype_config
    import aws_sdk_connectcampaignsv2.types.sms_channel_subtype_config
    import aws_sdk_connectcampaignsv2.types.telephony_channel_subtype_config
    import aws_sdk_connectcampaignsv2.types.whats_app_channel_subtype_config


class ChannelSubtypeConfig(TypedDict, closed=True):
    telephony: NotRequired[
        "aws_sdk_connectcampaignsv2.types.telephony_channel_subtype_config.TelephonyChannelSubtypeConfig"
    ]
    sms: NotRequired[
        "aws_sdk_connectcampaignsv2.types.sms_channel_subtype_config.SmsChannelSubtypeConfig"
    ]
    email: NotRequired[
        "aws_sdk_connectcampaignsv2.types.email_channel_subtype_config.EmailChannelSubtypeConfig"
    ]
    whats_app: NotRequired[
        "aws_sdk_connectcampaignsv2.types.whats_app_channel_subtype_config.WhatsAppChannelSubtypeConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelSubtypeConfig) -> dict:
    out: dict = {}
    if "telephony" in value:
        import aws_sdk_connectcampaignsv2.types.telephony_channel_subtype_config

        out["telephony"] = (
            aws_sdk_connectcampaignsv2.types.telephony_channel_subtype_config.serialize_json(
                value["telephony"]
            )
        )
    if "sms" in value:
        import aws_sdk_connectcampaignsv2.types.sms_channel_subtype_config

        out["sms"] = (
            aws_sdk_connectcampaignsv2.types.sms_channel_subtype_config.serialize_json(
                value["sms"]
            )
        )
    if "email" in value:
        import aws_sdk_connectcampaignsv2.types.email_channel_subtype_config

        out["email"] = (
            aws_sdk_connectcampaignsv2.types.email_channel_subtype_config.serialize_json(
                value["email"]
            )
        )
    if "whats_app" in value:
        import aws_sdk_connectcampaignsv2.types.whats_app_channel_subtype_config

        out["whatsApp"] = (
            aws_sdk_connectcampaignsv2.types.whats_app_channel_subtype_config.serialize_json(
                value["whats_app"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChannelSubtypeConfig:
    out: ChannelSubtypeConfig = {}  # type: ignore[typeddict-item]
    if "telephony" in data:
        import aws_sdk_connectcampaignsv2.types.telephony_channel_subtype_config

        out["telephony"] = (
            aws_sdk_connectcampaignsv2.types.telephony_channel_subtype_config.deserialize_json(
                data["telephony"]
            )
        )
    if "sms" in data:
        import aws_sdk_connectcampaignsv2.types.sms_channel_subtype_config

        out["sms"] = (
            aws_sdk_connectcampaignsv2.types.sms_channel_subtype_config.deserialize_json(
                data["sms"]
            )
        )
    if "email" in data:
        import aws_sdk_connectcampaignsv2.types.email_channel_subtype_config

        out["email"] = (
            aws_sdk_connectcampaignsv2.types.email_channel_subtype_config.deserialize_json(
                data["email"]
            )
        )
    if "whatsApp" in data:
        import aws_sdk_connectcampaignsv2.types.whats_app_channel_subtype_config

        out["whats_app"] = (
            aws_sdk_connectcampaignsv2.types.whats_app_channel_subtype_config.deserialize_json(
                data["whatsApp"]
            )
        )
    return out
