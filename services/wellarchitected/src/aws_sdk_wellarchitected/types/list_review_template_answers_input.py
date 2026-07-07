"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListReviewTemplateAnswersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.list_review_template_answers_max_results
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.pillar_id
    import aws_sdk_wellarchitected.types.template_arn


class ListReviewTemplateAnswersInput(TypedDict, closed=True):
    template_arn: "aws_sdk_wellarchitected.types.template_arn.TemplateArn"
    """<p>The ARN of the review template.</p>"""
    lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias"
    pillar_id: NotRequired["aws_sdk_wellarchitected.types.pillar_id.PillarId"]
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired[
        "aws_sdk_wellarchitected.types.list_review_template_answers_max_results.ListReviewTemplateAnswersMaxResults"
    ]
    """<p>The maximum number of results to return for this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReviewTemplateAnswersInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListReviewTemplateAnswersInput:
    out: ListReviewTemplateAnswersInput = {}  # type: ignore[typeddict-item]
    return out
