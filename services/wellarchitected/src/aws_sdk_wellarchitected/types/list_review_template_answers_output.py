"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListReviewTemplateAnswersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.review_template_answer_summaries
    import aws_sdk_wellarchitected.types.template_arn


class ListReviewTemplateAnswersOutput(TypedDict, closed=True):
    template_arn: NotRequired["aws_sdk_wellarchitected.types.template_arn.TemplateArn"]
    """<p>The ARN of the review template.</p>"""
    lens_alias: NotRequired["aws_sdk_wellarchitected.types.lens_alias.LensAlias"]
    answer_summaries: NotRequired[
        "aws_sdk_wellarchitected.types.review_template_answer_summaries.ReviewTemplateAnswerSummaries"
    ]
    """<p>List of answer summaries of a lens review in a review template.</p>"""
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListReviewTemplateAnswersOutput) -> dict:
    out: dict = {}
    if "template_arn" in value:
        out["TemplateArn"] = value["template_arn"]
    if "lens_alias" in value:
        out["LensAlias"] = value["lens_alias"]
    if "answer_summaries" in value:
        import aws_sdk_wellarchitected.types.review_template_answer_summaries

        out["AnswerSummaries"] = (
            aws_sdk_wellarchitected.types.review_template_answer_summaries.serialize_json(
                value["answer_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListReviewTemplateAnswersOutput:
    out: ListReviewTemplateAnswersOutput = {}  # type: ignore[typeddict-item]
    if "TemplateArn" in data:
        out["template_arn"] = data["TemplateArn"]
    if "LensAlias" in data:
        out["lens_alias"] = data["LensAlias"]
    if "AnswerSummaries" in data:
        import aws_sdk_wellarchitected.types.review_template_answer_summaries

        out["answer_summaries"] = (
            aws_sdk_wellarchitected.types.review_template_answer_summaries.deserialize_json(
                data["AnswerSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
