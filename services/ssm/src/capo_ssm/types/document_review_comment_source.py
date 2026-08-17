"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentReviewCommentSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.document_review_comment
    import capo_ssm.types.document_review_comment_type


class DocumentReviewCommentSource(TypedDict, closed=True):
    type: NotRequired[
        "capo_ssm.types.document_review_comment_type.DocumentReviewCommentType"
    ]
    """<p>The type of information added to a review request. Currently, only the value <code>Comment</code> is supported.</p>"""
    content: NotRequired["capo_ssm.types.document_review_comment.DocumentReviewComment"]
    """<p>The content of a comment entered by a user who requests a review of a new document version, or who reviews the new version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentReviewCommentSource) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_ssm.types.document_review_comment_type

        out["Type"] = (
            capo_ssm.types.document_review_comment_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "content" in value:
        out["Content"] = value["content"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentReviewCommentSource:
    out: DocumentReviewCommentSource = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_ssm.types.document_review_comment_type

        out["type"] = (
            capo_ssm.types.document_review_comment_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    return out
