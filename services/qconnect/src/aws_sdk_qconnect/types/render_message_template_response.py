"""Generated from Smithy shape ``com.amazonaws.qconnect#RenderMessageTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_attachment_list
    import aws_sdk_qconnect.types.message_template_attribute_key_list
    import aws_sdk_qconnect.types.message_template_content_provider
    import aws_sdk_qconnect.types.message_template_source_configuration_summary


class RenderMessageTemplateResponse(TypedDict):
    content: NotRequired[
        "aws_sdk_qconnect.types.message_template_content_provider.MessageTemplateContentProvider"
    ]
    """<p>The content of the message template.</p>"""
    source_configuration_summary: NotRequired[
        "aws_sdk_qconnect.types.message_template_source_configuration_summary.MessageTemplateSourceConfigurationSummary"
    ]
    """<p>The source configuration of the message template.</p>"""
    attributes_not_interpolated: NotRequired[
        "aws_sdk_qconnect.types.message_template_attribute_key_list.MessageTemplateAttributeKeyList"
    ]
    """<p>The attribute keys that are not resolved.</p>"""
    attachments: NotRequired[
        "aws_sdk_qconnect.types.message_template_attachment_list.MessageTemplateAttachmentList"
    ]
    """<p>The message template attachments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RenderMessageTemplateResponse) -> dict:
    out: dict = {}
    if "content" in value:
        import aws_sdk_qconnect.types.message_template_content_provider

        out["content"] = (
            aws_sdk_qconnect.types.message_template_content_provider.serialize_json(
                value["content"]
            )
        )
    if "source_configuration_summary" in value:
        import aws_sdk_qconnect.types.message_template_source_configuration_summary

        out["sourceConfigurationSummary"] = (
            aws_sdk_qconnect.types.message_template_source_configuration_summary.serialize_json(
                value["source_configuration_summary"]
            )
        )
    if "attributes_not_interpolated" in value:
        import aws_sdk_qconnect.types.message_template_attribute_key_list

        out["attributesNotInterpolated"] = (
            aws_sdk_qconnect.types.message_template_attribute_key_list.serialize_json(
                value["attributes_not_interpolated"]
            )
        )
    if "attachments" in value:
        import aws_sdk_qconnect.types.message_template_attachment_list

        out["attachments"] = (
            aws_sdk_qconnect.types.message_template_attachment_list.serialize_json(
                value["attachments"]
            )
        )
    return out


def deserialize_json(data: dict) -> RenderMessageTemplateResponse:
    out: RenderMessageTemplateResponse = {}  # type: ignore[typeddict-item]
    if "content" in data:
        import aws_sdk_qconnect.types.message_template_content_provider

        out["content"] = (
            aws_sdk_qconnect.types.message_template_content_provider.deserialize_json(
                data["content"]
            )
        )
    if "sourceConfigurationSummary" in data:
        import aws_sdk_qconnect.types.message_template_source_configuration_summary

        out["source_configuration_summary"] = (
            aws_sdk_qconnect.types.message_template_source_configuration_summary.deserialize_json(
                data["sourceConfigurationSummary"]
            )
        )
    if "attributesNotInterpolated" in data:
        import aws_sdk_qconnect.types.message_template_attribute_key_list

        out["attributes_not_interpolated"] = (
            aws_sdk_qconnect.types.message_template_attribute_key_list.deserialize_json(
                data["attributesNotInterpolated"]
            )
        )
    if "attachments" in data:
        import aws_sdk_qconnect.types.message_template_attachment_list

        out["attachments"] = (
            aws_sdk_qconnect.types.message_template_attachment_list.deserialize_json(
                data["attachments"]
            )
        )
    return out
