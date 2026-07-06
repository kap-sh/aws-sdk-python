"""Generated from Smithy shape ``com.amazonaws.pinpoint#DirectMessageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.adm_message
    import aws_sdk_pinpoint.types.apns_message
    import aws_sdk_pinpoint.types.baidu_message
    import aws_sdk_pinpoint.types.default_message
    import aws_sdk_pinpoint.types.default_push_notification_message
    import aws_sdk_pinpoint.types.email_message
    import aws_sdk_pinpoint.types.gcm_message
    import aws_sdk_pinpoint.types.sms_message
    import aws_sdk_pinpoint.types.voice_message


class DirectMessageConfiguration(TypedDict, closed=True):
    adm_message: NotRequired["aws_sdk_pinpoint.types.adm_message.ADMMessage"]
    """<p>The default push notification message for the ADM (Amazon Device Messaging) channel. This message overrides the default push notification message (DefaultPushNotificationMessage).</p>"""
    apns_message: NotRequired["aws_sdk_pinpoint.types.apns_message.APNSMessage"]
    """<p>The default push notification message for the APNs (Apple Push Notification service) channel. This message overrides the default push notification message (DefaultPushNotificationMessage).</p>"""
    baidu_message: NotRequired["aws_sdk_pinpoint.types.baidu_message.BaiduMessage"]
    """<p>The default push notification message for the Baidu (Baidu Cloud Push) channel. This message overrides the default push notification message (DefaultPushNotificationMessage).</p>"""
    default_message: NotRequired[
        "aws_sdk_pinpoint.types.default_message.DefaultMessage"
    ]
    """<p>The default message for all channels.</p>"""
    default_push_notification_message: NotRequired[
        "aws_sdk_pinpoint.types.default_push_notification_message.DefaultPushNotificationMessage"
    ]
    """<p>The default push notification message for all push notification channels.</p>"""
    email_message: NotRequired["aws_sdk_pinpoint.types.email_message.EmailMessage"]
    """<p>The default message for the email channel. This message overrides the default message (DefaultMessage).</p>"""
    gcm_message: NotRequired["aws_sdk_pinpoint.types.gcm_message.GCMMessage"]
    """<p>The default push notification message for the GCM channel, which is used to send notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service. This message overrides the default push notification message (DefaultPushNotificationMessage).</p>"""
    sms_message: NotRequired["aws_sdk_pinpoint.types.sms_message.SMSMessage"]
    """<p>The default message for the SMS channel. This message overrides the default message (DefaultMessage).</p>"""
    voice_message: NotRequired["aws_sdk_pinpoint.types.voice_message.VoiceMessage"]
    """<p>The default message for the voice channel. This message overrides the default message (DefaultMessage).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DirectMessageConfiguration) -> dict:
    out: dict = {}
    if "adm_message" in value:
        import aws_sdk_pinpoint.types.adm_message

        out["ADMMessage"] = aws_sdk_pinpoint.types.adm_message.serialize_json(
            value["adm_message"]
        )
    if "apns_message" in value:
        import aws_sdk_pinpoint.types.apns_message

        out["APNSMessage"] = aws_sdk_pinpoint.types.apns_message.serialize_json(
            value["apns_message"]
        )
    if "baidu_message" in value:
        import aws_sdk_pinpoint.types.baidu_message

        out["BaiduMessage"] = aws_sdk_pinpoint.types.baidu_message.serialize_json(
            value["baidu_message"]
        )
    if "default_message" in value:
        import aws_sdk_pinpoint.types.default_message

        out["DefaultMessage"] = aws_sdk_pinpoint.types.default_message.serialize_json(
            value["default_message"]
        )
    if "default_push_notification_message" in value:
        import aws_sdk_pinpoint.types.default_push_notification_message

        out["DefaultPushNotificationMessage"] = (
            aws_sdk_pinpoint.types.default_push_notification_message.serialize_json(
                value["default_push_notification_message"]
            )
        )
    if "email_message" in value:
        import aws_sdk_pinpoint.types.email_message

        out["EmailMessage"] = aws_sdk_pinpoint.types.email_message.serialize_json(
            value["email_message"]
        )
    if "gcm_message" in value:
        import aws_sdk_pinpoint.types.gcm_message

        out["GCMMessage"] = aws_sdk_pinpoint.types.gcm_message.serialize_json(
            value["gcm_message"]
        )
    if "sms_message" in value:
        import aws_sdk_pinpoint.types.sms_message

        out["SMSMessage"] = aws_sdk_pinpoint.types.sms_message.serialize_json(
            value["sms_message"]
        )
    if "voice_message" in value:
        import aws_sdk_pinpoint.types.voice_message

        out["VoiceMessage"] = aws_sdk_pinpoint.types.voice_message.serialize_json(
            value["voice_message"]
        )
    return out


def deserialize_json(data: dict) -> DirectMessageConfiguration:
    out: DirectMessageConfiguration = {}  # type: ignore[typeddict-item]
    if "ADMMessage" in data:
        import aws_sdk_pinpoint.types.adm_message

        out["adm_message"] = aws_sdk_pinpoint.types.adm_message.deserialize_json(
            data["ADMMessage"]
        )
    if "APNSMessage" in data:
        import aws_sdk_pinpoint.types.apns_message

        out["apns_message"] = aws_sdk_pinpoint.types.apns_message.deserialize_json(
            data["APNSMessage"]
        )
    if "BaiduMessage" in data:
        import aws_sdk_pinpoint.types.baidu_message

        out["baidu_message"] = aws_sdk_pinpoint.types.baidu_message.deserialize_json(
            data["BaiduMessage"]
        )
    if "DefaultMessage" in data:
        import aws_sdk_pinpoint.types.default_message

        out["default_message"] = (
            aws_sdk_pinpoint.types.default_message.deserialize_json(
                data["DefaultMessage"]
            )
        )
    if "DefaultPushNotificationMessage" in data:
        import aws_sdk_pinpoint.types.default_push_notification_message

        out["default_push_notification_message"] = (
            aws_sdk_pinpoint.types.default_push_notification_message.deserialize_json(
                data["DefaultPushNotificationMessage"]
            )
        )
    if "EmailMessage" in data:
        import aws_sdk_pinpoint.types.email_message

        out["email_message"] = aws_sdk_pinpoint.types.email_message.deserialize_json(
            data["EmailMessage"]
        )
    if "GCMMessage" in data:
        import aws_sdk_pinpoint.types.gcm_message

        out["gcm_message"] = aws_sdk_pinpoint.types.gcm_message.deserialize_json(
            data["GCMMessage"]
        )
    if "SMSMessage" in data:
        import aws_sdk_pinpoint.types.sms_message

        out["sms_message"] = aws_sdk_pinpoint.types.sms_message.deserialize_json(
            data["SMSMessage"]
        )
    if "VoiceMessage" in data:
        import aws_sdk_pinpoint.types.voice_message

        out["voice_message"] = aws_sdk_pinpoint.types.voice_message.deserialize_json(
            data["VoiceMessage"]
        )
    return out
