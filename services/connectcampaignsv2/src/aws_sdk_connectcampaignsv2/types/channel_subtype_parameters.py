"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#ChannelSubtypeParameters``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.email_channel_subtype_parameters
    import aws_sdk_connectcampaignsv2.types.sms_channel_subtype_parameters
    import aws_sdk_connectcampaignsv2.types.telephony_channel_subtype_parameters
    import aws_sdk_connectcampaignsv2.types.whats_app_channel_subtype_parameters


class _ChannelSubtypeParameters_telephony(TypedDict):
    telephony: "aws_sdk_connectcampaignsv2.types.telephony_channel_subtype_parameters.TelephonyChannelSubtypeParameters"


class _ChannelSubtypeParameters_sms(TypedDict):
    sms: "aws_sdk_connectcampaignsv2.types.sms_channel_subtype_parameters.SmsChannelSubtypeParameters"


class _ChannelSubtypeParameters_email(TypedDict):
    email: "aws_sdk_connectcampaignsv2.types.email_channel_subtype_parameters.EmailChannelSubtypeParameters"


class _ChannelSubtypeParameters_whatsApp(TypedDict):
    whatsApp: "aws_sdk_connectcampaignsv2.types.whats_app_channel_subtype_parameters.WhatsAppChannelSubtypeParameters"


ChannelSubtypeParameters: TypeAlias = (
    _ChannelSubtypeParameters_telephony
    | _ChannelSubtypeParameters_sms
    | _ChannelSubtypeParameters_email
    | _ChannelSubtypeParameters_whatsApp
)


# --- restJson1 ser/de ---
def serialize_json(value: ChannelSubtypeParameters) -> dict:
    if "telephony" in value:
        import aws_sdk_connectcampaignsv2.types.telephony_channel_subtype_parameters

        return {
            "telephony": aws_sdk_connectcampaignsv2.types.telephony_channel_subtype_parameters.serialize_json(
                value["telephony"]
            )
        }
    elif "sms" in value:
        import aws_sdk_connectcampaignsv2.types.sms_channel_subtype_parameters

        return {
            "sms": aws_sdk_connectcampaignsv2.types.sms_channel_subtype_parameters.serialize_json(
                value["sms"]
            )
        }
    elif "email" in value:
        import aws_sdk_connectcampaignsv2.types.email_channel_subtype_parameters

        return {
            "email": aws_sdk_connectcampaignsv2.types.email_channel_subtype_parameters.serialize_json(
                value["email"]
            )
        }
    elif "whatsApp" in value:
        import aws_sdk_connectcampaignsv2.types.whats_app_channel_subtype_parameters

        return {
            "whatsApp": aws_sdk_connectcampaignsv2.types.whats_app_channel_subtype_parameters.serialize_json(
                value["whatsApp"]
            )
        }
    else:
        raise SerializationError("ChannelSubtypeParameters: no variant present")


def deserialize_json(data: dict) -> ChannelSubtypeParameters:
    if "telephony" in data:
        import aws_sdk_connectcampaignsv2.types.telephony_channel_subtype_parameters

        return {
            "telephony": aws_sdk_connectcampaignsv2.types.telephony_channel_subtype_parameters.deserialize_json(
                data["telephony"]
            )
        }
    elif "sms" in data:
        import aws_sdk_connectcampaignsv2.types.sms_channel_subtype_parameters

        return {
            "sms": aws_sdk_connectcampaignsv2.types.sms_channel_subtype_parameters.deserialize_json(
                data["sms"]
            )
        }
    elif "email" in data:
        import aws_sdk_connectcampaignsv2.types.email_channel_subtype_parameters

        return {
            "email": aws_sdk_connectcampaignsv2.types.email_channel_subtype_parameters.deserialize_json(
                data["email"]
            )
        }
    elif "whatsApp" in data:
        import aws_sdk_connectcampaignsv2.types.whats_app_channel_subtype_parameters

        return {
            "whatsApp": aws_sdk_connectcampaignsv2.types.whats_app_channel_subtype_parameters.deserialize_json(
                data["whatsApp"]
            )
        }
    else:
        raise DeserializationError(
            "ChannelSubtypeParameters: no recognized variant key"
        )
