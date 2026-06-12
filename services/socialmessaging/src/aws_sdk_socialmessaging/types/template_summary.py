"""Generated from Smithy shape ``com.amazonaws.socialmessaging#TemplateSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.meta_template_category
    import aws_sdk_socialmessaging.types.meta_template_id
    import aws_sdk_socialmessaging.types.meta_template_language
    import aws_sdk_socialmessaging.types.meta_template_name
    import aws_sdk_socialmessaging.types.meta_template_quality_score
    import aws_sdk_socialmessaging.types.meta_template_status


class TemplateSummary(TypedDict):
    template_name: NotRequired[
        "aws_sdk_socialmessaging.types.meta_template_name.MetaTemplateName"
    ]
    """<p>The name of the template.</p>"""
    meta_template_id: NotRequired[
        "aws_sdk_socialmessaging.types.meta_template_id.MetaTemplateId"
    ]
    """<p>The numeric ID assigned to the template by Meta.</p>"""
    template_status: NotRequired[
        "aws_sdk_socialmessaging.types.meta_template_status.MetaTemplateStatus"
    ]
    """<p>The current status of the template (for example, APPROVED, PENDING, or REJECTED).</p>"""
    template_quality_score: NotRequired[
        "aws_sdk_socialmessaging.types.meta_template_quality_score.MetaTemplateQualityScore"
    ]
    """<p>The quality score assigned to the template by Meta.</p>"""
    template_language: NotRequired[
        "aws_sdk_socialmessaging.types.meta_template_language.MetaTemplateLanguage"
    ]
    """<p>The language code of the template (for example, en_US).</p>"""
    template_category: NotRequired[
        "aws_sdk_socialmessaging.types.meta_template_category.MetaTemplateCategory"
    ]
    """<p>The category of the template (for example, UTILITY or MARKETING).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateSummary) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["templateName"] = value["template_name"]
    if "meta_template_id" in value:
        out["metaTemplateId"] = value["meta_template_id"]
    if "template_status" in value:
        out["templateStatus"] = value["template_status"]
    if "template_quality_score" in value:
        out["templateQualityScore"] = value["template_quality_score"]
    if "template_language" in value:
        out["templateLanguage"] = value["template_language"]
    if "template_category" in value:
        out["templateCategory"] = value["template_category"]
    return out


def deserialize_json(data: dict) -> TemplateSummary:
    out: TemplateSummary = {}  # type: ignore[typeddict-item]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    if "metaTemplateId" in data:
        out["meta_template_id"] = data["metaTemplateId"]
    if "templateStatus" in data:
        out["template_status"] = data["templateStatus"]
    if "templateQualityScore" in data:
        out["template_quality_score"] = data["templateQualityScore"]
    if "templateLanguage" in data:
        out["template_language"] = data["templateLanguage"]
    if "templateCategory" in data:
        out["template_category"] = data["templateCategory"]
    return out
