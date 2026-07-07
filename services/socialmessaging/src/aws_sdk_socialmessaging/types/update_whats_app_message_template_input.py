"""Generated from Smithy shape ``com.amazonaws.socialmessaging#UpdateWhatsAppMessageTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.linked_whats_app_business_account_id
    import aws_sdk_socialmessaging.types.meta_parameter_format
    import aws_sdk_socialmessaging.types.meta_template_category
    import aws_sdk_socialmessaging.types.meta_template_components
    import aws_sdk_socialmessaging.types.meta_template_cta_link_tracking_opted_out
    import aws_sdk_socialmessaging.types.meta_template_id
    import aws_sdk_socialmessaging.types.meta_template_language
    import aws_sdk_socialmessaging.types.meta_template_name


class UpdateWhatsAppMessageTemplateInput(TypedDict, closed=True):
    id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account associated with this template.</p>"""
    meta_template_id: NotRequired[
        "aws_sdk_socialmessaging.types.meta_template_id.MetaTemplateId"
    ]
    """<p>The numeric ID of the template assigned by Meta.</p>"""
    template_name: NotRequired[
        "aws_sdk_socialmessaging.types.meta_template_name.MetaTemplateName"
    ]
    """<p>The name of the message template. Use together with <code>templateLanguageCode</code> as an alternative to <code>metaTemplateId</code> to identify a template.</p>"""
    template_language_code: NotRequired[
        "aws_sdk_socialmessaging.types.meta_template_language.MetaTemplateLanguage"
    ]
    """<p>The language code of the message template (for example, <code>en</code> or <code>en_US</code>). Use together with <code>templateName</code> as an alternative to <code>metaTemplateId</code> to identify a template.</p>"""
    parameter_format: NotRequired[
        "aws_sdk_socialmessaging.types.meta_parameter_format.MetaParameterFormat"
    ]
    """<p>The format specification for parameters in the template, this can be either 'named' or 'positional'.</p>"""
    template_category: NotRequired[
        "aws_sdk_socialmessaging.types.meta_template_category.MetaTemplateCategory"
    ]
    """<p>The new category for the template (for example, UTILITY or MARKETING).</p>"""
    template_components: NotRequired[
        "aws_sdk_socialmessaging.types.meta_template_components.MetaTemplateComponents"
    ]
    """<p>The updated components of the template as a JSON blob (maximum 3000 characters).</p>"""
    cta_url_link_tracking_opted_out: NotRequired[
        "aws_sdk_socialmessaging.types.meta_template_cta_link_tracking_opted_out.MetaTemplateCtaLinkTrackingOptedOut"
    ]
    """<p>When true, disables click tracking for call-to-action URL buttons in the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWhatsAppMessageTemplateInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "meta_template_id" in value:
        out["metaTemplateId"] = value["meta_template_id"]
    if "template_name" in value:
        out["templateName"] = value["template_name"]
    if "template_language_code" in value:
        out["templateLanguageCode"] = value["template_language_code"]
    if "parameter_format" in value:
        out["parameterFormat"] = value["parameter_format"]
    if "template_category" in value:
        out["templateCategory"] = value["template_category"]
    if "template_components" in value:
        import aws_sdk_socialmessaging.types.meta_template_components

        out["templateComponents"] = (
            aws_sdk_socialmessaging.types.meta_template_components.serialize_json(
                value["template_components"]
            )
        )
    if "cta_url_link_tracking_opted_out" in value:
        out["ctaUrlLinkTrackingOptedOut"] = value["cta_url_link_tracking_opted_out"]
    return out


def deserialize_json(data: dict) -> UpdateWhatsAppMessageTemplateInput:
    out: UpdateWhatsAppMessageTemplateInput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateWhatsAppMessageTemplateInput.id required")
    if "metaTemplateId" in data:
        out["meta_template_id"] = data["metaTemplateId"]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    if "templateLanguageCode" in data:
        out["template_language_code"] = data["templateLanguageCode"]
    if "parameterFormat" in data:
        out["parameter_format"] = data["parameterFormat"]
    if "templateCategory" in data:
        out["template_category"] = data["templateCategory"]
    if "templateComponents" in data:
        import aws_sdk_socialmessaging.types.meta_template_components

        out["template_components"] = (
            aws_sdk_socialmessaging.types.meta_template_components.deserialize_json(
                data["templateComponents"]
            )
        )
    if "ctaUrlLinkTrackingOptedOut" in data:
        out["cta_url_link_tracking_opted_out"] = data["ctaUrlLinkTrackingOptedOut"]
    return out
