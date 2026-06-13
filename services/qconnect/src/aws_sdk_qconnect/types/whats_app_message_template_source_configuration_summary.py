"""Generated from Smithy shape ``com.amazonaws.qconnect#WhatsAppMessageTemplateSourceConfigurationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.non_empty_unlimited_string
    import aws_sdk_qconnect.types.whats_app_business_account_id
    import aws_sdk_qconnect.types.whats_app_message_template_components
    import aws_sdk_qconnect.types.whats_app_message_template_id
    import aws_sdk_qconnect.types.whats_app_message_template_language
    import aws_sdk_qconnect.types.whats_app_message_template_name
    import aws_sdk_qconnect.types.whats_app_source_configuration_status


class WhatsAppMessageTemplateSourceConfigurationSummary(TypedDict):
    business_account_id: (
        "aws_sdk_qconnect.types.whats_app_business_account_id.WhatsAppBusinessAccountId"
    )
    """<p>The ID of the End User Messaging WhatsApp Business Account to associate with this template.</p>"""
    template_id: (
        "aws_sdk_qconnect.types.whats_app_message_template_id.WhatsAppMessageTemplateId"
    )
    """<p>The ID of WhatsApp template.</p>"""
    name: NotRequired[
        "aws_sdk_qconnect.types.whats_app_message_template_name.WhatsAppMessageTemplateName"
    ]
    """<p>The name of the WhatsApp template.</p>"""
    language: NotRequired[
        "aws_sdk_qconnect.types.whats_app_message_template_language.WhatsAppMessageTemplateLanguage"
    ]
    """<p>The language of the WhatsApp template.</p>"""
    components: NotRequired[
        "aws_sdk_qconnect.types.whats_app_message_template_components.WhatsAppMessageTemplateComponents"
    ]
    """<p>The list of component mapping from WhatsApp template parameters to Message Template attributes.</p>"""
    status: NotRequired[
        "aws_sdk_qconnect.types.whats_app_source_configuration_status.WhatsAppSourceConfigurationStatus"
    ]
    """<p>The status of the message template.</p>"""
    status_reason: NotRequired[
        "aws_sdk_qconnect.types.non_empty_unlimited_string.NonEmptyUnlimitedString"
    ]
    """<p>The status reason of the message template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppMessageTemplateSourceConfigurationSummary) -> dict:
    out: dict = {}
    out["businessAccountId"] = value["business_account_id"]
    out["templateId"] = value["template_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "language" in value:
        out["language"] = value["language"]
    if "components" in value:
        import aws_sdk_qconnect.types.whats_app_message_template_components

        out["components"] = (
            aws_sdk_qconnect.types.whats_app_message_template_components.serialize_json(
                value["components"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> WhatsAppMessageTemplateSourceConfigurationSummary:
    out: WhatsAppMessageTemplateSourceConfigurationSummary = {}  # type: ignore[typeddict-item]
    if "businessAccountId" in data:
        out["business_account_id"] = data["businessAccountId"]
    else:
        raise DeserializationError(
            "WhatsAppMessageTemplateSourceConfigurationSummary.business_account_id required"
        )
    if "templateId" in data:
        out["template_id"] = data["templateId"]
    else:
        raise DeserializationError(
            "WhatsAppMessageTemplateSourceConfigurationSummary.template_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    if "language" in data:
        out["language"] = data["language"]
    if "components" in data:
        import aws_sdk_qconnect.types.whats_app_message_template_components

        out["components"] = (
            aws_sdk_qconnect.types.whats_app_message_template_components.deserialize_json(
                data["components"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
