"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentReviews``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_review_action
    import aws_sdk_ssm.types.document_review_comment_list


class DocumentReviews(TypedDict, closed=True):
    action: "aws_sdk_ssm.types.document_review_action.DocumentReviewAction"
    """<p>The action to take on a document approval review request.</p>"""
    comment: NotRequired[
        "aws_sdk_ssm.types.document_review_comment_list.DocumentReviewCommentList"
    ]
    """<p>A comment entered by a user in your organization about the document review request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentReviews) -> dict:
    out: dict = {}
    import aws_sdk_ssm.types.document_review_action

    out["Action"] = aws_sdk_ssm.types.document_review_action.serialize_aws_json_1_1(
        value["action"]
    )
    if "comment" in value:
        import aws_sdk_ssm.types.document_review_comment_list

        out["Comment"] = (
            aws_sdk_ssm.types.document_review_comment_list.serialize_aws_json_1_1(
                value["comment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentReviews:
    out: DocumentReviews = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_ssm.types.document_review_action

        out["action"] = (
            aws_sdk_ssm.types.document_review_action.deserialize_aws_json_1_1(
                data["Action"]
            )
        )
    else:
        raise DeserializationError("DocumentReviews.action required")
    if "Comment" in data:
        import aws_sdk_ssm.types.document_review_comment_list

        out["comment"] = (
            aws_sdk_ssm.types.document_review_comment_list.deserialize_aws_json_1_1(
                data["Comment"]
            )
        )
    return out
