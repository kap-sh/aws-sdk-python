"""Generated from Smithy shape ``com.amazonaws.qconnect#RenderMessageTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_attachment_list
    import capo_qconnect.types.message_template_attribute_key_list
    import capo_qconnect.types.message_template_content_provider
    import capo_qconnect.types.message_template_source_configuration_summary


class RenderMessageTemplateResponse(TypedDict, closed=True):
    content: NotRequired[
        "capo_qconnect.types.message_template_content_provider.MessageTemplateContentProvider"
    ]
    """<p>The content of the message template.</p>"""
    source_configuration_summary: NotRequired[
        "capo_qconnect.types.message_template_source_configuration_summary.MessageTemplateSourceConfigurationSummary"
    ]
    """<p>The source configuration of the message template.</p>"""
    attributes_not_interpolated: NotRequired[
        "capo_qconnect.types.message_template_attribute_key_list.MessageTemplateAttributeKeyList"
    ]
    """<p>The attribute keys that are not resolved.</p>"""
    attachments: NotRequired[
        "capo_qconnect.types.message_template_attachment_list.MessageTemplateAttachmentList"
    ]
    """<p>The message template attachments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RenderMessageTemplateResponse) -> dict:
    out: dict = {}
    if "content" in value:
        import capo_qconnect.types.message_template_content_provider

        out["content"] = (
            capo_qconnect.types.message_template_content_provider.serialize_json(
                value["content"]
            )
        )
    if "source_configuration_summary" in value:
        import capo_qconnect.types.message_template_source_configuration_summary

        out["sourceConfigurationSummary"] = (
            capo_qconnect.types.message_template_source_configuration_summary.serialize_json(
                value["source_configuration_summary"]
            )
        )
    if "attributes_not_interpolated" in value:
        import capo_qconnect.types.message_template_attribute_key_list

        out["attributesNotInterpolated"] = (
            capo_qconnect.types.message_template_attribute_key_list.serialize_json(
                value["attributes_not_interpolated"]
            )
        )
    if "attachments" in value:
        import capo_qconnect.types.message_template_attachment_list

        out["attachments"] = (
            capo_qconnect.types.message_template_attachment_list.serialize_json(
                value["attachments"]
            )
        )
    return out


def deserialize_json(data: dict) -> RenderMessageTemplateResponse:
    out: RenderMessageTemplateResponse = {}  # type: ignore[typeddict-item]
    if "content" in data:
        import capo_qconnect.types.message_template_content_provider

        out["content"] = (
            capo_qconnect.types.message_template_content_provider.deserialize_json(
                data["content"]
            )
        )
    if "sourceConfigurationSummary" in data:
        import capo_qconnect.types.message_template_source_configuration_summary

        out["source_configuration_summary"] = (
            capo_qconnect.types.message_template_source_configuration_summary.deserialize_json(
                data["sourceConfigurationSummary"]
            )
        )
    if "attributesNotInterpolated" in data:
        import capo_qconnect.types.message_template_attribute_key_list

        out["attributes_not_interpolated"] = (
            capo_qconnect.types.message_template_attribute_key_list.deserialize_json(
                data["attributesNotInterpolated"]
            )
        )
    if "attachments" in data:
        import capo_qconnect.types.message_template_attachment_list

        out["attachments"] = (
            capo_qconnect.types.message_template_attachment_list.deserialize_json(
                data["attachments"]
            )
        )
    return out
