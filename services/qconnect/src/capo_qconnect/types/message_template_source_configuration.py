"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateSourceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qconnect.types.whats_app_message_template_source_configuration


class _MessageTemplateSourceConfiguration_whatsApp(TypedDict, closed=True):
    whatsApp: "capo_qconnect.types.whats_app_message_template_source_configuration.WhatsAppMessageTemplateSourceConfiguration"


MessageTemplateSourceConfiguration: TypeAlias = (
    _MessageTemplateSourceConfiguration_whatsApp
)


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateSourceConfiguration) -> dict:
    if "whatsApp" in value:
        import capo_qconnect.types.whats_app_message_template_source_configuration

        return {
            "whatsApp": capo_qconnect.types.whats_app_message_template_source_configuration.serialize_json(
                value["whatsApp"]
            )
        }
    else:
        raise SerializationError(
            "MessageTemplateSourceConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> MessageTemplateSourceConfiguration:
    if "whatsApp" in data:
        import capo_qconnect.types.whats_app_message_template_source_configuration

        return {
            "whatsApp": capo_qconnect.types.whats_app_message_template_source_configuration.deserialize_json(
                data["whatsApp"]
            )
        }
    else:
        raise DeserializationError(
            "MessageTemplateSourceConfiguration: no recognized variant key"
        )
