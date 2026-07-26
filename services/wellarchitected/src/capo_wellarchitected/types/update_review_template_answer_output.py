"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateReviewTemplateAnswerOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_alias
    import capo_wellarchitected.types.review_template_answer
    import capo_wellarchitected.types.template_arn


class UpdateReviewTemplateAnswerOutput(TypedDict, closed=True):
    template_arn: NotRequired["capo_wellarchitected.types.template_arn.TemplateArn"]
    """<p>The review template ARN.</p>"""
    lens_alias: NotRequired["capo_wellarchitected.types.lens_alias.LensAlias"]
    answer: NotRequired[
        "capo_wellarchitected.types.review_template_answer.ReviewTemplateAnswer"
    ]
    """<p>An answer of the question.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReviewTemplateAnswerOutput) -> dict:
    out: dict = {}
    if "template_arn" in value:
        out["TemplateArn"] = value["template_arn"]
    if "lens_alias" in value:
        out["LensAlias"] = value["lens_alias"]
    if "answer" in value:
        import capo_wellarchitected.types.review_template_answer

        out["Answer"] = (
            capo_wellarchitected.types.review_template_answer.serialize_json(
                value["answer"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateReviewTemplateAnswerOutput:
    out: UpdateReviewTemplateAnswerOutput = {}  # type: ignore[typeddict-item]
    if "TemplateArn" in data:
        out["template_arn"] = data["TemplateArn"]
    if "LensAlias" in data:
        out["lens_alias"] = data["LensAlias"]
    if "Answer" in data:
        import capo_wellarchitected.types.review_template_answer

        out["answer"] = (
            capo_wellarchitected.types.review_template_answer.deserialize_json(
                data["Answer"]
            )
        )
    return out
