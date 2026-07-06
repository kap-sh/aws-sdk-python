"""Generated from Smithy shape ``com.amazonaws.pinpoint#MessageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.campaign_custom_message
    import aws_sdk_pinpoint.types.campaign_email_message
    import aws_sdk_pinpoint.types.campaign_in_app_message
    import aws_sdk_pinpoint.types.campaign_sms_message
    import aws_sdk_pinpoint.types.message


class MessageConfiguration(TypedDict, closed=True):
    adm_message: NotRequired["aws_sdk_pinpoint.types.message.Message"]
    """<p>The message that the campaign sends through the ADM (Amazon Device Messaging) channel. If specified, this message overrides the default message.</p>"""
    apns_message: NotRequired["aws_sdk_pinpoint.types.message.Message"]
    """<p>The message that the campaign sends through the APNs (Apple Push Notification service) channel. If specified, this message overrides the default message.</p>"""
    baidu_message: NotRequired["aws_sdk_pinpoint.types.message.Message"]
    """<p>The message that the campaign sends through the Baidu (Baidu Cloud Push) channel. If specified, this message overrides the default message.</p>"""
    custom_message: NotRequired[
        "aws_sdk_pinpoint.types.campaign_custom_message.CampaignCustomMessage"
    ]
    """<p>The message that the campaign sends through a custom channel, as specified by the delivery configuration (CustomDeliveryConfiguration) settings for the campaign. If specified, this message overrides the default message.</p>"""
    default_message: NotRequired["aws_sdk_pinpoint.types.message.Message"]
    """<p>The default message that the campaign sends through all the channels that are configured for the campaign.</p>"""
    email_message: NotRequired[
        "aws_sdk_pinpoint.types.campaign_email_message.CampaignEmailMessage"
    ]
    """<p>The message that the campaign sends through the email channel. If specified, this message overrides the default message.</p>"""
    gcm_message: NotRequired["aws_sdk_pinpoint.types.message.Message"]
    """<p>The message that the campaign sends through the GCM channel, which enables Amazon Pinpoint to send push notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service. If specified, this message overrides the default message.</p>"""
    sms_message: NotRequired[
        "aws_sdk_pinpoint.types.campaign_sms_message.CampaignSmsMessage"
    ]
    """<p>The message that the campaign sends through the SMS channel. If specified, this message overrides the default message.</p>"""
    in_app_message: NotRequired[
        "aws_sdk_pinpoint.types.campaign_in_app_message.CampaignInAppMessage"
    ]
    """<p>The in-app message configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageConfiguration) -> dict:
    out: dict = {}
    if "adm_message" in value:
        import aws_sdk_pinpoint.types.message

        out["ADMMessage"] = aws_sdk_pinpoint.types.message.serialize_json(
            value["adm_message"]
        )
    if "apns_message" in value:
        import aws_sdk_pinpoint.types.message

        out["APNSMessage"] = aws_sdk_pinpoint.types.message.serialize_json(
            value["apns_message"]
        )
    if "baidu_message" in value:
        import aws_sdk_pinpoint.types.message

        out["BaiduMessage"] = aws_sdk_pinpoint.types.message.serialize_json(
            value["baidu_message"]
        )
    if "custom_message" in value:
        import aws_sdk_pinpoint.types.campaign_custom_message

        out["CustomMessage"] = (
            aws_sdk_pinpoint.types.campaign_custom_message.serialize_json(
                value["custom_message"]
            )
        )
    if "default_message" in value:
        import aws_sdk_pinpoint.types.message

        out["DefaultMessage"] = aws_sdk_pinpoint.types.message.serialize_json(
            value["default_message"]
        )
    if "email_message" in value:
        import aws_sdk_pinpoint.types.campaign_email_message

        out["EmailMessage"] = (
            aws_sdk_pinpoint.types.campaign_email_message.serialize_json(
                value["email_message"]
            )
        )
    if "gcm_message" in value:
        import aws_sdk_pinpoint.types.message

        out["GCMMessage"] = aws_sdk_pinpoint.types.message.serialize_json(
            value["gcm_message"]
        )
    if "sms_message" in value:
        import aws_sdk_pinpoint.types.campaign_sms_message

        out["SMSMessage"] = aws_sdk_pinpoint.types.campaign_sms_message.serialize_json(
            value["sms_message"]
        )
    if "in_app_message" in value:
        import aws_sdk_pinpoint.types.campaign_in_app_message

        out["InAppMessage"] = (
            aws_sdk_pinpoint.types.campaign_in_app_message.serialize_json(
                value["in_app_message"]
            )
        )
    return out


def deserialize_json(data: dict) -> MessageConfiguration:
    out: MessageConfiguration = {}  # type: ignore[typeddict-item]
    if "ADMMessage" in data:
        import aws_sdk_pinpoint.types.message

        out["adm_message"] = aws_sdk_pinpoint.types.message.deserialize_json(
            data["ADMMessage"]
        )
    if "APNSMessage" in data:
        import aws_sdk_pinpoint.types.message

        out["apns_message"] = aws_sdk_pinpoint.types.message.deserialize_json(
            data["APNSMessage"]
        )
    if "BaiduMessage" in data:
        import aws_sdk_pinpoint.types.message

        out["baidu_message"] = aws_sdk_pinpoint.types.message.deserialize_json(
            data["BaiduMessage"]
        )
    if "CustomMessage" in data:
        import aws_sdk_pinpoint.types.campaign_custom_message

        out["custom_message"] = (
            aws_sdk_pinpoint.types.campaign_custom_message.deserialize_json(
                data["CustomMessage"]
            )
        )
    if "DefaultMessage" in data:
        import aws_sdk_pinpoint.types.message

        out["default_message"] = aws_sdk_pinpoint.types.message.deserialize_json(
            data["DefaultMessage"]
        )
    if "EmailMessage" in data:
        import aws_sdk_pinpoint.types.campaign_email_message

        out["email_message"] = (
            aws_sdk_pinpoint.types.campaign_email_message.deserialize_json(
                data["EmailMessage"]
            )
        )
    if "GCMMessage" in data:
        import aws_sdk_pinpoint.types.message

        out["gcm_message"] = aws_sdk_pinpoint.types.message.deserialize_json(
            data["GCMMessage"]
        )
    if "SMSMessage" in data:
        import aws_sdk_pinpoint.types.campaign_sms_message

        out["sms_message"] = (
            aws_sdk_pinpoint.types.campaign_sms_message.deserialize_json(
                data["SMSMessage"]
            )
        )
    if "InAppMessage" in data:
        import aws_sdk_pinpoint.types.campaign_in_app_message

        out["in_app_message"] = (
            aws_sdk_pinpoint.types.campaign_in_app_message.deserialize_json(
                data["InAppMessage"]
            )
        )
    return out
