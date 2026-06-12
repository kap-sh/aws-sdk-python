"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RecommendationFeedback``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.arn
    import aws_sdk_codeguru_reviewer.types.reactions
    import aws_sdk_codeguru_reviewer.types.recommendation_id
    import aws_sdk_codeguru_reviewer.types.time_stamp
    import aws_sdk_codeguru_reviewer.types.user_id


class RecommendationFeedback(TypedDict):
    code_review_arn: NotRequired["aws_sdk_codeguru_reviewer.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html\">CodeReview</a> object. </p>"""
    recommendation_id: NotRequired[
        "aws_sdk_codeguru_reviewer.types.recommendation_id.RecommendationId"
    ]
    """<p>The recommendation ID that can be used to track the provided recommendations. Later on it can be used to collect the feedback.</p>"""
    reactions: NotRequired["aws_sdk_codeguru_reviewer.types.reactions.Reactions"]
    """<p>List for storing reactions. Reactions are utf-8 text code for emojis. You can send an empty list to clear off all your feedback.</p>"""
    user_id: NotRequired["aws_sdk_codeguru_reviewer.types.user_id.UserId"]
    """<p>The ID of the user that made the API call.</p> <p> The <code>UserId</code> is an IAM principal that can be specified as an Amazon Web Services account ID or an Amazon Resource Name (ARN). For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying\"> Specifying a Principal</a> in the <i>Amazon Web Services Identity and Access Management User Guide</i>.</p>"""
    created_time_stamp: NotRequired[
        "aws_sdk_codeguru_reviewer.types.time_stamp.TimeStamp"
    ]
    """<p>The time at which the feedback was created.</p>"""
    last_updated_time_stamp: NotRequired[
        "aws_sdk_codeguru_reviewer.types.time_stamp.TimeStamp"
    ]
    """<p>The time at which the feedback was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationFeedback) -> dict:
    out: dict = {}
    if "code_review_arn" in value:
        out["CodeReviewArn"] = value["code_review_arn"]
    if "recommendation_id" in value:
        out["RecommendationId"] = value["recommendation_id"]
    if "reactions" in value:
        import aws_sdk_codeguru_reviewer.types.reactions

        out["Reactions"] = aws_sdk_codeguru_reviewer.types.reactions.serialize_json(
            value["reactions"]
        )
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "created_time_stamp" in value:
        import aws_sdk_codeguru_reviewer.types.time_stamp

        out["CreatedTimeStamp"] = (
            aws_sdk_codeguru_reviewer.types.time_stamp.serialize_json(
                value["created_time_stamp"]
            )
        )
    if "last_updated_time_stamp" in value:
        import aws_sdk_codeguru_reviewer.types.time_stamp

        out["LastUpdatedTimeStamp"] = (
            aws_sdk_codeguru_reviewer.types.time_stamp.serialize_json(
                value["last_updated_time_stamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecommendationFeedback:
    out: RecommendationFeedback = {}  # type: ignore[typeddict-item]
    if "CodeReviewArn" in data:
        out["code_review_arn"] = data["CodeReviewArn"]
    if "RecommendationId" in data:
        out["recommendation_id"] = data["RecommendationId"]
    if "Reactions" in data:
        import aws_sdk_codeguru_reviewer.types.reactions

        out["reactions"] = aws_sdk_codeguru_reviewer.types.reactions.deserialize_json(
            data["Reactions"]
        )
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "CreatedTimeStamp" in data:
        import aws_sdk_codeguru_reviewer.types.time_stamp

        out["created_time_stamp"] = (
            aws_sdk_codeguru_reviewer.types.time_stamp.deserialize_json(
                data["CreatedTimeStamp"]
            )
        )
    if "LastUpdatedTimeStamp" in data:
        import aws_sdk_codeguru_reviewer.types.time_stamp

        out["last_updated_time_stamp"] = (
            aws_sdk_codeguru_reviewer.types.time_stamp.deserialize_json(
                data["LastUpdatedTimeStamp"]
            )
        )
    return out
