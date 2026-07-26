"""Generated from Smithy shape ``com.amazonaws.socialmessaging#DeleteWhatsAppMessageTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.delete_all_languages
    import capo_socialmessaging.types.linked_whats_app_business_account_id
    import capo_socialmessaging.types.meta_template_id
    import capo_socialmessaging.types.meta_template_name


class DeleteWhatsAppMessageTemplateInput(TypedDict, closed=True):
    meta_template_id: NotRequired[
        "capo_socialmessaging.types.meta_template_id.MetaTemplateId"
    ]
    """<p>The numeric ID of the template assigned by Meta.</p>"""
    delete_all_languages: NotRequired[
        "capo_socialmessaging.types.delete_all_languages.DeleteAllLanguages"
    ]
    """<p>If true, deletes all language versions of the template.</p>"""
    id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account associated with this template.</p>"""
    template_name: "capo_socialmessaging.types.meta_template_name.MetaTemplateName"
    """<p>The name of the template to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWhatsAppMessageTemplateInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWhatsAppMessageTemplateInput:
    out: DeleteWhatsAppMessageTemplateInput = {}  # type: ignore[typeddict-item]
    return out
