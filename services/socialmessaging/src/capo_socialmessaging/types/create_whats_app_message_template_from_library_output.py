"""Generated from Smithy shape ``com.amazonaws.socialmessaging#CreateWhatsAppMessageTemplateFromLibraryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_template_category
    import capo_socialmessaging.types.meta_template_id


class CreateWhatsAppMessageTemplateFromLibraryOutput(TypedDict, closed=True):
    meta_template_id: NotRequired[
        "capo_socialmessaging.types.meta_template_id.MetaTemplateId"
    ]
    """<p>The numeric ID assigned to the template by Meta.</p>"""
    template_status: NotRequired["str"]
    """<p>The status of the created template (for example, PENDING or APPROVED).</p>"""
    category: NotRequired[
        "capo_socialmessaging.types.meta_template_category.MetaTemplateCategory"
    ]
    """<p>The category of the template (for example, UTILITY or MARKETING).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWhatsAppMessageTemplateFromLibraryOutput) -> dict:
    out: dict = {}
    if "meta_template_id" in value:
        out["metaTemplateId"] = value["meta_template_id"]
    if "template_status" in value:
        out["templateStatus"] = value["template_status"]
    if "category" in value:
        out["category"] = value["category"]
    return out


def deserialize_json(data: dict) -> CreateWhatsAppMessageTemplateFromLibraryOutput:
    out: CreateWhatsAppMessageTemplateFromLibraryOutput = {}  # type: ignore[typeddict-item]
    if "metaTemplateId" in data:
        out["meta_template_id"] = data["metaTemplateId"]
    if "templateStatus" in data:
        out["template_status"] = data["templateStatus"]
    if "category" in data:
        out["category"] = data["category"]
    return out
