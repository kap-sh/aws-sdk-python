"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateContentProvider``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qconnect.types.email_message_template_content
    import capo_qconnect.types.push_message_template_content
    import capo_qconnect.types.sms_message_template_content
    import capo_qconnect.types.whats_app_message_template_content


class _MessageTemplateContentProvider_email(TypedDict, closed=True):
    email: (
        "capo_qconnect.types.email_message_template_content.EmailMessageTemplateContent"
    )


class _MessageTemplateContentProvider_sms(TypedDict, closed=True):
    sms: "capo_qconnect.types.sms_message_template_content.SMSMessageTemplateContent"


class _MessageTemplateContentProvider_whatsApp(TypedDict, closed=True):
    whatsApp: "capo_qconnect.types.whats_app_message_template_content.WhatsAppMessageTemplateContent"


class _MessageTemplateContentProvider_push(TypedDict, closed=True):
    push: "capo_qconnect.types.push_message_template_content.PushMessageTemplateContent"


MessageTemplateContentProvider: TypeAlias = (
    _MessageTemplateContentProvider_email
    | _MessageTemplateContentProvider_sms
    | _MessageTemplateContentProvider_whatsApp
    | _MessageTemplateContentProvider_push
)


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateContentProvider) -> dict:
    if "email" in value:
        import capo_qconnect.types.email_message_template_content

        return {
            "email": capo_qconnect.types.email_message_template_content.serialize_json(
                value["email"]
            )
        }
    elif "sms" in value:
        import capo_qconnect.types.sms_message_template_content

        return {
            "sms": capo_qconnect.types.sms_message_template_content.serialize_json(
                value["sms"]
            )
        }
    elif "whatsApp" in value:
        import capo_qconnect.types.whats_app_message_template_content

        return {
            "whatsApp": capo_qconnect.types.whats_app_message_template_content.serialize_json(
                value["whatsApp"]
            )
        }
    elif "push" in value:
        import capo_qconnect.types.push_message_template_content

        return {
            "push": capo_qconnect.types.push_message_template_content.serialize_json(
                value["push"]
            )
        }
    else:
        raise SerializationError("MessageTemplateContentProvider: no variant present")


def deserialize_json(data: dict) -> MessageTemplateContentProvider:
    if "email" in data:
        import capo_qconnect.types.email_message_template_content

        return {
            "email": capo_qconnect.types.email_message_template_content.deserialize_json(
                data["email"]
            )
        }
    elif "sms" in data:
        import capo_qconnect.types.sms_message_template_content

        return {
            "sms": capo_qconnect.types.sms_message_template_content.deserialize_json(
                data["sms"]
            )
        }
    elif "whatsApp" in data:
        import capo_qconnect.types.whats_app_message_template_content

        return {
            "whatsApp": capo_qconnect.types.whats_app_message_template_content.deserialize_json(
                data["whatsApp"]
            )
        }
    elif "push" in data:
        import capo_qconnect.types.push_message_template_content

        return {
            "push": capo_qconnect.types.push_message_template_content.deserialize_json(
                data["push"]
            )
        }
    else:
        raise DeserializationError(
            "MessageTemplateContentProvider: no recognized variant key"
        )
