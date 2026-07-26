"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetReviewTemplateAnswerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_alias
    import capo_wellarchitected.types.question_id
    import capo_wellarchitected.types.template_arn


class GetReviewTemplateAnswerInput(TypedDict, closed=True):
    template_arn: "capo_wellarchitected.types.template_arn.TemplateArn"
    """<p>The review template ARN.</p>"""
    lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias"
    question_id: "capo_wellarchitected.types.question_id.QuestionId"


# --- restJson1 ser/de ---
def serialize_json(value: GetReviewTemplateAnswerInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReviewTemplateAnswerInput:
    out: GetReviewTemplateAnswerInput = {}  # type: ignore[typeddict-item]
    return out
