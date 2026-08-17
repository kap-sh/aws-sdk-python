"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentReviewerResponseSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.date_time
    import capo_ssm.types.document_review_comment_list
    import capo_ssm.types.review_status
    import capo_ssm.types.reviewer


class DocumentReviewerResponseSource(TypedDict, closed=True):
    create_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date and time that a reviewer entered a response to a document review request.</p>"""
    updated_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date and time that a reviewer last updated a response to a document review request.</p>"""
    review_status: NotRequired["capo_ssm.types.review_status.ReviewStatus"]
    """<p>The current review status of a new custom SSM document created by a member of your organization, or of the latest version of an existing SSM document.</p> <p>Only one version of a document can be in the APPROVED state at a time. When a new version is approved, the status of the previous version changes to REJECTED.</p> <p>Only one version of a document can be in review, or PENDING, at a time.</p>"""
    comment: NotRequired[
        "capo_ssm.types.document_review_comment_list.DocumentReviewCommentList"
    ]
    """<p>The comment entered by a reviewer as part of their document review response.</p>"""
    reviewer: NotRequired["capo_ssm.types.reviewer.Reviewer"]
    """<p>The user in your organization assigned to review a document request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentReviewerResponseSource) -> dict:
    out: dict = {}
    if "create_time" in value:
        import capo_ssm.types.date_time

        out["CreateTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "updated_time" in value:
        import capo_ssm.types.date_time

        out["UpdatedTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["updated_time"]
        )
    if "review_status" in value:
        import capo_ssm.types.review_status

        out["ReviewStatus"] = capo_ssm.types.review_status.serialize_aws_json_1_1(
            value["review_status"]
        )
    if "comment" in value:
        import capo_ssm.types.document_review_comment_list

        out["Comment"] = (
            capo_ssm.types.document_review_comment_list.serialize_aws_json_1_1(
                value["comment"]
            )
        )
    if "reviewer" in value:
        out["Reviewer"] = value["reviewer"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentReviewerResponseSource:
    out: DocumentReviewerResponseSource = {}  # type: ignore[typeddict-item]
    if data.get("CreateTime") is not None:
        import capo_ssm.types.date_time

        out["create_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreateTime"]
        )
    if data.get("UpdatedTime") is not None:
        import capo_ssm.types.date_time

        out["updated_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["UpdatedTime"]
        )
    if data.get("ReviewStatus") is not None:
        import capo_ssm.types.review_status

        out["review_status"] = capo_ssm.types.review_status.deserialize_aws_json_1_1(
            data["ReviewStatus"]
        )
    if data.get("Comment") is not None:
        import capo_ssm.types.document_review_comment_list

        out["comment"] = (
            capo_ssm.types.document_review_comment_list.deserialize_aws_json_1_1(
                data["Comment"]
            )
        )
    if data.get("Reviewer") is not None:
        out["reviewer"] = data["Reviewer"]
    return out
