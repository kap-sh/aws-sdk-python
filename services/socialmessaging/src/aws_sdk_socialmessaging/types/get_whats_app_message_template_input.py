"""Generated from Smithy shape ``com.amazonaws.socialmessaging#GetWhatsAppMessageTemplateInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.linked_whats_app_business_account_id
    import aws_sdk_socialmessaging.types.meta_template_id
    import aws_sdk_socialmessaging.types.meta_template_language
    import aws_sdk_socialmessaging.types.meta_template_name


class GetWhatsAppMessageTemplateInput(TypedDict):
    meta_template_id: NotRequired[
        "aws_sdk_socialmessaging.types.meta_template_id.MetaTemplateId"
    ]
    """<p>The numeric ID of the template assigned by Meta.</p>"""
    id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account associated with this template.</p>"""
    template_name: NotRequired[
        "aws_sdk_socialmessaging.types.meta_template_name.MetaTemplateName"
    ]
    """<p>The name of the message template. Use together with <code>templateLanguageCode</code> as an alternative to <code>metaTemplateId</code> to identify a template.</p>"""
    template_language_code: NotRequired[
        "aws_sdk_socialmessaging.types.meta_template_language.MetaTemplateLanguage"
    ]
    """<p>The language code of the message template (for example, <code>en</code> or <code>en_US</code>). Use together with <code>templateName</code> as an alternative to <code>metaTemplateId</code> to identify a template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWhatsAppMessageTemplateInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWhatsAppMessageTemplateInput:
    out: GetWhatsAppMessageTemplateInput = {}  # type: ignore[typeddict-item]
    return out
