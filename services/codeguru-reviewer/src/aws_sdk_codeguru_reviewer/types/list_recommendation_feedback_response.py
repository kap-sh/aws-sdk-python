"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#ListRecommendationFeedbackResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.next_token
    import aws_sdk_codeguru_reviewer.types.recommendation_feedback_summaries


class ListRecommendationFeedbackResponse(TypedDict):
    recommendation_feedback_summaries: NotRequired[
        "aws_sdk_codeguru_reviewer.types.recommendation_feedback_summaries.RecommendationFeedbackSummaries"
    ]
    """<p>Recommendation feedback summaries corresponding to the code review ARN.</p>"""
    next_token: NotRequired["aws_sdk_codeguru_reviewer.types.next_token.NextToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationFeedbackResponse) -> dict:
    out: dict = {}
    if "recommendation_feedback_summaries" in value:
        import aws_sdk_codeguru_reviewer.types.recommendation_feedback_summaries

        out["RecommendationFeedbackSummaries"] = (
            aws_sdk_codeguru_reviewer.types.recommendation_feedback_summaries.serialize_json(
                value["recommendation_feedback_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecommendationFeedbackResponse:
    out: ListRecommendationFeedbackResponse = {}  # type: ignore[typeddict-item]
    if "RecommendationFeedbackSummaries" in data:
        import aws_sdk_codeguru_reviewer.types.recommendation_feedback_summaries

        out["recommendation_feedback_summaries"] = (
            aws_sdk_codeguru_reviewer.types.recommendation_feedback_summaries.deserialize_json(
                data["RecommendationFeedbackSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
