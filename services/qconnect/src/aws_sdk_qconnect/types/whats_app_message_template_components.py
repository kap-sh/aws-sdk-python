"""Generated from Smithy shape ``com.amazonaws.qconnect#WhatsAppMessageTemplateComponents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.whats_app_message_template_component

WhatsAppMessageTemplateComponents: TypeAlias = list[
    "aws_sdk_qconnect.types.whats_app_message_template_component.WhatsAppMessageTemplateComponent"
]


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppMessageTemplateComponents) -> list:
    return list(value)


def deserialize_json(data: list) -> WhatsAppMessageTemplateComponents:
    return list(data)
