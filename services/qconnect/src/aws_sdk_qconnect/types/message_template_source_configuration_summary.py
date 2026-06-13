"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateSourceConfigurationSummary``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.whats_app_message_template_source_configuration_summary


class _MessageTemplateSourceConfigurationSummary_whatsApp(TypedDict):
    whatsApp: "aws_sdk_qconnect.types.whats_app_message_template_source_configuration_summary.WhatsAppMessageTemplateSourceConfigurationSummary"


MessageTemplateSourceConfigurationSummary: TypeAlias = (
    _MessageTemplateSourceConfigurationSummary_whatsApp
)


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateSourceConfigurationSummary) -> dict:
    if "whatsApp" in value:
        import aws_sdk_qconnect.types.whats_app_message_template_source_configuration_summary

        return {
            "whatsApp": aws_sdk_qconnect.types.whats_app_message_template_source_configuration_summary.serialize_json(
                value["whatsApp"]
            )
        }
    else:
        raise SerializationError(
            "MessageTemplateSourceConfigurationSummary: no variant present"
        )


def deserialize_json(data: dict) -> MessageTemplateSourceConfigurationSummary:
    if "whatsApp" in data:
        import aws_sdk_qconnect.types.whats_app_message_template_source_configuration_summary

        return {
            "whatsApp": aws_sdk_qconnect.types.whats_app_message_template_source_configuration_summary.deserialize_json(
                data["whatsApp"]
            )
        }
    else:
        raise DeserializationError(
            "MessageTemplateSourceConfigurationSummary: no recognized variant key"
        )
