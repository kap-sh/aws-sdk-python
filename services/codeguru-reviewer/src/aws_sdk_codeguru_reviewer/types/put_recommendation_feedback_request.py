"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#PutRecommendationFeedbackRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeguru_reviewer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.arn
    import aws_sdk_codeguru_reviewer.types.reactions
    import aws_sdk_codeguru_reviewer.types.recommendation_id


class PutRecommendationFeedbackRequest(TypedDict):
    code_review_arn: "aws_sdk_codeguru_reviewer.types.arn.Arn"
    r"""<p>The Amazon Resource Name (ARN) of the <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html\">CodeReview</a> object. </p>"""
    recommendation_id: (
        "aws_sdk_codeguru_reviewer.types.recommendation_id.RecommendationId"
    )
    """<p>The recommendation ID that can be used to track the provided recommendations and then to collect the feedback.</p>"""
    reactions: "aws_sdk_codeguru_reviewer.types.reactions.Reactions"
    """<p>List for storing reactions. Reactions are utf-8 text code for emojis. If you send an empty list it clears all your feedback.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRecommendationFeedbackRequest) -> dict:
    out: dict = {}
    out["CodeReviewArn"] = value["code_review_arn"]
    out["RecommendationId"] = value["recommendation_id"]
    import aws_sdk_codeguru_reviewer.types.reactions

    out["Reactions"] = aws_sdk_codeguru_reviewer.types.reactions.serialize_json(
        value["reactions"]
    )
    return out


def deserialize_json(data: dict) -> PutRecommendationFeedbackRequest:
    out: PutRecommendationFeedbackRequest = {}  # type: ignore[typeddict-item]
    if "CodeReviewArn" in data:
        out["code_review_arn"] = data["CodeReviewArn"]
    else:
        raise DeserializationError(
            "PutRecommendationFeedbackRequest.code_review_arn required"
        )
    if "RecommendationId" in data:
        out["recommendation_id"] = data["RecommendationId"]
    else:
        raise DeserializationError(
            "PutRecommendationFeedbackRequest.recommendation_id required"
        )
    if "Reactions" in data:
        import aws_sdk_codeguru_reviewer.types.reactions

        out["reactions"] = aws_sdk_codeguru_reviewer.types.reactions.deserialize_json(
            data["Reactions"]
        )
    else:
        raise DeserializationError(
            "PutRecommendationFeedbackRequest.reactions required"
        )
    return out
