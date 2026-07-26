"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetReviewTemplateLensReviewOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.review_template_lens_review
    import capo_wellarchitected.types.template_arn


class GetReviewTemplateLensReviewOutput(TypedDict, closed=True):
    template_arn: NotRequired["capo_wellarchitected.types.template_arn.TemplateArn"]
    """<p>The review template ARN.</p>"""
    lens_review: NotRequired[
        "capo_wellarchitected.types.review_template_lens_review.ReviewTemplateLensReview"
    ]
    """<p>A lens review of a question.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReviewTemplateLensReviewOutput) -> dict:
    out: dict = {}
    if "template_arn" in value:
        out["TemplateArn"] = value["template_arn"]
    if "lens_review" in value:
        import capo_wellarchitected.types.review_template_lens_review

        out["LensReview"] = (
            capo_wellarchitected.types.review_template_lens_review.serialize_json(
                value["lens_review"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetReviewTemplateLensReviewOutput:
    out: GetReviewTemplateLensReviewOutput = {}  # type: ignore[typeddict-item]
    if "TemplateArn" in data:
        out["template_arn"] = data["TemplateArn"]
    if "LensReview" in data:
        import capo_wellarchitected.types.review_template_lens_review

        out["lens_review"] = (
            capo_wellarchitected.types.review_template_lens_review.deserialize_json(
                data["LensReview"]
            )
        )
    return out
