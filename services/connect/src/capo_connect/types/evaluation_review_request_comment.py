"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationReviewRequestComment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.evaluation_review_request_comment_content
    import capo_connect.types.timestamp


class EvaluationReviewRequestComment(TypedDict, closed=True):
    comment: NotRequired[
        "capo_connect.types.evaluation_review_request_comment_content.EvaluationReviewRequestCommentContent"
    ]
    """<p>The text content of the review request comment.</p>"""
    created_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the evaluation review request comment was created.</p>"""
    created_by: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The user who created the evaluation review request comment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationReviewRequestComment) -> dict:
    out: dict = {}
    if "comment" in value:
        out["Comment"] = value["comment"]
    if "created_time" in value:
        import capo_connect.types.timestamp

        out["CreatedTime"] = capo_connect.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    return out


def deserialize_json(data: dict) -> EvaluationReviewRequestComment:
    out: EvaluationReviewRequestComment = {}  # type: ignore[typeddict-item]
    if "Comment" in data:
        out["comment"] = data["Comment"]
    if "CreatedTime" in data:
        import capo_connect.types.timestamp

        out["created_time"] = capo_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    return out
