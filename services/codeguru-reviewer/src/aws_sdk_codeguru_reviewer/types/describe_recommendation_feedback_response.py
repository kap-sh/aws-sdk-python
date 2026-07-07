"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#DescribeRecommendationFeedbackResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.recommendation_feedback


class DescribeRecommendationFeedbackResponse(TypedDict, closed=True):
    recommendation_feedback: NotRequired[
        "aws_sdk_codeguru_reviewer.types.recommendation_feedback.RecommendationFeedback"
    ]
    """<p>The recommendation feedback given by the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRecommendationFeedbackResponse) -> dict:
    out: dict = {}
    if "recommendation_feedback" in value:
        import aws_sdk_codeguru_reviewer.types.recommendation_feedback

        out["RecommendationFeedback"] = (
            aws_sdk_codeguru_reviewer.types.recommendation_feedback.serialize_json(
                value["recommendation_feedback"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeRecommendationFeedbackResponse:
    out: DescribeRecommendationFeedbackResponse = {}  # type: ignore[typeddict-item]
    if "RecommendationFeedback" in data:
        import aws_sdk_codeguru_reviewer.types.recommendation_feedback

        out["recommendation_feedback"] = (
            aws_sdk_codeguru_reviewer.types.recommendation_feedback.deserialize_json(
                data["RecommendationFeedback"]
            )
        )
    return out
