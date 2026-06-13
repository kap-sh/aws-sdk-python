"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateContentProvider``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.email_message_template_content
    import aws_sdk_qconnect.types.push_message_template_content
    import aws_sdk_qconnect.types.sms_message_template_content
    import aws_sdk_qconnect.types.whats_app_message_template_content


class _MessageTemplateContentProvider_email(TypedDict):
    email: "aws_sdk_qconnect.types.email_message_template_content.EmailMessageTemplateContent"


class _MessageTemplateContentProvider_sms(TypedDict):
    sms: "aws_sdk_qconnect.types.sms_message_template_content.SMSMessageTemplateContent"


class _MessageTemplateContentProvider_whatsApp(TypedDict):
    whatsApp: "aws_sdk_qconnect.types.whats_app_message_template_content.WhatsAppMessageTemplateContent"


class _MessageTemplateContentProvider_push(TypedDict):
    push: "aws_sdk_qconnect.types.push_message_template_content.PushMessageTemplateContent"


MessageTemplateContentProvider: TypeAlias = (
    _MessageTemplateContentProvider_email
    | _MessageTemplateContentProvider_sms
    | _MessageTemplateContentProvider_whatsApp
    | _MessageTemplateContentProvider_push
)


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateContentProvider) -> dict:
    if "email" in value:
        import aws_sdk_qconnect.types.email_message_template_content

        return {
            "email": aws_sdk_qconnect.types.email_message_template_content.serialize_json(
                value["email"]
            )
        }
    elif "sms" in value:
        import aws_sdk_qconnect.types.sms_message_template_content

        return {
            "sms": aws_sdk_qconnect.types.sms_message_template_content.serialize_json(
                value["sms"]
            )
        }
    elif "whatsApp" in value:
        import aws_sdk_qconnect.types.whats_app_message_template_content

        return {
            "whatsApp": aws_sdk_qconnect.types.whats_app_message_template_content.serialize_json(
                value["whatsApp"]
            )
        }
    elif "push" in value:
        import aws_sdk_qconnect.types.push_message_template_content

        return {
            "push": aws_sdk_qconnect.types.push_message_template_content.serialize_json(
                value["push"]
            )
        }
    else:
        raise SerializationError("MessageTemplateContentProvider: no variant present")


def deserialize_json(data: dict) -> MessageTemplateContentProvider:
    if "email" in data:
        import aws_sdk_qconnect.types.email_message_template_content

        return {
            "email": aws_sdk_qconnect.types.email_message_template_content.deserialize_json(
                data["email"]
            )
        }
    elif "sms" in data:
        import aws_sdk_qconnect.types.sms_message_template_content

        return {
            "sms": aws_sdk_qconnect.types.sms_message_template_content.deserialize_json(
                data["sms"]
            )
        }
    elif "whatsApp" in data:
        import aws_sdk_qconnect.types.whats_app_message_template_content

        return {
            "whatsApp": aws_sdk_qconnect.types.whats_app_message_template_content.deserialize_json(
                data["whatsApp"]
            )
        }
    elif "push" in data:
        import aws_sdk_qconnect.types.push_message_template_content

        return {
            "push": aws_sdk_qconnect.types.push_message_template_content.deserialize_json(
                data["push"]
            )
        }
    else:
        raise DeserializationError(
            "MessageTemplateContentProvider: no recognized variant key"
        )
