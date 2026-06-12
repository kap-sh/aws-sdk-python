"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationReviewRequestCommentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_review_request_comment

EvaluationReviewRequestCommentList: TypeAlias = list[
    "aws_sdk_connect.types.evaluation_review_request_comment.EvaluationReviewRequestComment"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationReviewRequestCommentList) -> list:
    import aws_sdk_connect.types.evaluation_review_request_comment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.evaluation_review_request_comment.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EvaluationReviewRequestCommentList:
    import aws_sdk_connect.types.evaluation_review_request_comment

    out: EvaluationReviewRequestCommentList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.evaluation_review_request_comment.deserialize_json(
                item
            )
        )
    return out
