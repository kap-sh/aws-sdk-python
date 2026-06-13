"""Generated from Smithy shape ``com.amazonaws.qconnect#PushMessageTemplateContent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.push_adm_message_template_content
    import aws_sdk_qconnect.types.push_apns_message_template_content
    import aws_sdk_qconnect.types.push_baidu_message_template_content
    import aws_sdk_qconnect.types.push_fcm_message_template_content


class PushMessageTemplateContent(TypedDict):
    adm: NotRequired[
        "aws_sdk_qconnect.types.push_adm_message_template_content.PushADMMessageTemplateContent"
    ]
    """<p>The content of the message template that applies to ADM (Amazon Device Messaging) notification service.</p>"""
    apns: NotRequired[
        "aws_sdk_qconnect.types.push_apns_message_template_content.PushAPNSMessageTemplateContent"
    ]
    """<p>The content of the message template that applies to APNS(Apple Push Notification service) notification service.</p>"""
    fcm: NotRequired[
        "aws_sdk_qconnect.types.push_fcm_message_template_content.PushFCMMessageTemplateContent"
    ]
    """<p>The content of the message template that applies to FCM (Firebase Cloud Messaging) notification service.</p>"""
    baidu: NotRequired[
        "aws_sdk_qconnect.types.push_baidu_message_template_content.PushBaiduMessageTemplateContent"
    ]
    """<p>The content of the message template that applies to Baidu notification service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PushMessageTemplateContent) -> dict:
    out: dict = {}
    if "adm" in value:
        import aws_sdk_qconnect.types.push_adm_message_template_content

        out["adm"] = (
            aws_sdk_qconnect.types.push_adm_message_template_content.serialize_json(
                value["adm"]
            )
        )
    if "apns" in value:
        import aws_sdk_qconnect.types.push_apns_message_template_content

        out["apns"] = (
            aws_sdk_qconnect.types.push_apns_message_template_content.serialize_json(
                value["apns"]
            )
        )
    if "fcm" in value:
        import aws_sdk_qconnect.types.push_fcm_message_template_content

        out["fcm"] = (
            aws_sdk_qconnect.types.push_fcm_message_template_content.serialize_json(
                value["fcm"]
            )
        )
    if "baidu" in value:
        import aws_sdk_qconnect.types.push_baidu_message_template_content

        out["baidu"] = (
            aws_sdk_qconnect.types.push_baidu_message_template_content.serialize_json(
                value["baidu"]
            )
        )
    return out


def deserialize_json(data: dict) -> PushMessageTemplateContent:
    out: PushMessageTemplateContent = {}  # type: ignore[typeddict-item]
    if "adm" in data:
        import aws_sdk_qconnect.types.push_adm_message_template_content

        out["adm"] = (
            aws_sdk_qconnect.types.push_adm_message_template_content.deserialize_json(
                data["adm"]
            )
        )
    if "apns" in data:
        import aws_sdk_qconnect.types.push_apns_message_template_content

        out["apns"] = (
            aws_sdk_qconnect.types.push_apns_message_template_content.deserialize_json(
                data["apns"]
            )
        )
    if "fcm" in data:
        import aws_sdk_qconnect.types.push_fcm_message_template_content

        out["fcm"] = (
            aws_sdk_qconnect.types.push_fcm_message_template_content.deserialize_json(
                data["fcm"]
            )
        )
    if "baidu" in data:
        import aws_sdk_qconnect.types.push_baidu_message_template_content

        out["baidu"] = (
            aws_sdk_qconnect.types.push_baidu_message_template_content.deserialize_json(
                data["baidu"]
            )
        )
    return out
