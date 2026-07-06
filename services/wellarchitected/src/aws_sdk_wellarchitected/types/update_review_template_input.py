"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateReviewTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.notes
    import aws_sdk_wellarchitected.types.review_template_lens_aliases
    import aws_sdk_wellarchitected.types.template_arn
    import aws_sdk_wellarchitected.types.template_description
    import aws_sdk_wellarchitected.types.template_name


class UpdateReviewTemplateInput(TypedDict, closed=True):
    template_arn: "aws_sdk_wellarchitected.types.template_arn.TemplateArn"
    """<p>The review template ARN.</p>"""
    template_name: NotRequired[
        "aws_sdk_wellarchitected.types.template_name.TemplateName"
    ]
    """<p>The review template name.</p>"""
    description: NotRequired[
        "aws_sdk_wellarchitected.types.template_description.TemplateDescription"
    ]
    """<p>The review template description.</p>"""
    notes: NotRequired["aws_sdk_wellarchitected.types.notes.Notes"]
    lenses_to_associate: NotRequired[
        "aws_sdk_wellarchitected.types.review_template_lens_aliases.ReviewTemplateLensAliases"
    ]
    """<p>A list of lens aliases or ARNs to apply to the review template.</p>"""
    lenses_to_disassociate: NotRequired[
        "aws_sdk_wellarchitected.types.review_template_lens_aliases.ReviewTemplateLensAliases"
    ]
    """<p>A list of lens aliases or ARNs to unapply to the review template. The <code>wellarchitected</code> lens cannot be unapplied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReviewTemplateInput) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "lenses_to_associate" in value:
        import aws_sdk_wellarchitected.types.review_template_lens_aliases

        out["LensesToAssociate"] = (
            aws_sdk_wellarchitected.types.review_template_lens_aliases.serialize_json(
                value["lenses_to_associate"]
            )
        )
    if "lenses_to_disassociate" in value:
        import aws_sdk_wellarchitected.types.review_template_lens_aliases

        out["LensesToDisassociate"] = (
            aws_sdk_wellarchitected.types.review_template_lens_aliases.serialize_json(
                value["lenses_to_disassociate"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateReviewTemplateInput:
    out: UpdateReviewTemplateInput = {}  # type: ignore[typeddict-item]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Notes" in data:
        out["notes"] = data["Notes"]
    if "LensesToAssociate" in data:
        import aws_sdk_wellarchitected.types.review_template_lens_aliases

        out["lenses_to_associate"] = (
            aws_sdk_wellarchitected.types.review_template_lens_aliases.deserialize_json(
                data["LensesToAssociate"]
            )
        )
    if "LensesToDisassociate" in data:
        import aws_sdk_wellarchitected.types.review_template_lens_aliases

        out["lenses_to_disassociate"] = (
            aws_sdk_wellarchitected.types.review_template_lens_aliases.deserialize_json(
                data["LensesToDisassociate"]
            )
        )
    return out
