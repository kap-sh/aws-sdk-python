"""Generated from Smithy shape ``com.amazonaws.mturk#ListReviewPolicyResultsForHITResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mturk.types.entity_id
    import aws_sdk_mturk.types.pagination_token
    import aws_sdk_mturk.types.review_policy
    import aws_sdk_mturk.types.review_report


class ListReviewPolicyResultsForHITResponse(TypedDict):
    hit_id: NotRequired["aws_sdk_mturk.types.entity_id.EntityId"]
    """<p>The HITId of the HIT for which results have been returned.</p>"""
    assignment_review_policy: NotRequired[
        "aws_sdk_mturk.types.review_policy.ReviewPolicy"
    ]
    """<p> The name of the Assignment-level Review Policy. This contains only the PolicyName element. </p>"""
    hit_review_policy: NotRequired["aws_sdk_mturk.types.review_policy.ReviewPolicy"]
    """<p>The name of the HIT-level Review Policy. This contains only the PolicyName element.</p>"""
    assignment_review_report: NotRequired[
        "aws_sdk_mturk.types.review_report.ReviewReport"
    ]
    """<p> Contains both ReviewResult and ReviewAction elements for an Assignment. </p>"""
    hit_review_report: NotRequired["aws_sdk_mturk.types.review_report.ReviewReport"]
    """<p>Contains both ReviewResult and ReviewAction elements for a particular HIT. </p>"""
    next_token: NotRequired["aws_sdk_mturk.types.pagination_token.PaginationToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReviewPolicyResultsForHITResponse) -> dict:
    out: dict = {}
    if "hit_id" in value:
        out["HITId"] = value["hit_id"]
    if "assignment_review_policy" in value:
        import aws_sdk_mturk.types.review_policy

        out["AssignmentReviewPolicy"] = (
            aws_sdk_mturk.types.review_policy.serialize_aws_json_1_1(
                value["assignment_review_policy"]
            )
        )
    if "hit_review_policy" in value:
        import aws_sdk_mturk.types.review_policy

        out["HITReviewPolicy"] = (
            aws_sdk_mturk.types.review_policy.serialize_aws_json_1_1(
                value["hit_review_policy"]
            )
        )
    if "assignment_review_report" in value:
        import aws_sdk_mturk.types.review_report

        out["AssignmentReviewReport"] = (
            aws_sdk_mturk.types.review_report.serialize_aws_json_1_1(
                value["assignment_review_report"]
            )
        )
    if "hit_review_report" in value:
        import aws_sdk_mturk.types.review_report

        out["HITReviewReport"] = (
            aws_sdk_mturk.types.review_report.serialize_aws_json_1_1(
                value["hit_review_report"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReviewPolicyResultsForHITResponse:
    out: ListReviewPolicyResultsForHITResponse = {}  # type: ignore[typeddict-item]
    if "HITId" in data:
        out["hit_id"] = data["HITId"]
    if "AssignmentReviewPolicy" in data:
        import aws_sdk_mturk.types.review_policy

        out["assignment_review_policy"] = (
            aws_sdk_mturk.types.review_policy.deserialize_aws_json_1_1(
                data["AssignmentReviewPolicy"]
            )
        )
    if "HITReviewPolicy" in data:
        import aws_sdk_mturk.types.review_policy

        out["hit_review_policy"] = (
            aws_sdk_mturk.types.review_policy.deserialize_aws_json_1_1(
                data["HITReviewPolicy"]
            )
        )
    if "AssignmentReviewReport" in data:
        import aws_sdk_mturk.types.review_report

        out["assignment_review_report"] = (
            aws_sdk_mturk.types.review_report.deserialize_aws_json_1_1(
                data["AssignmentReviewReport"]
            )
        )
    if "HITReviewReport" in data:
        import aws_sdk_mturk.types.review_report

        out["hit_review_report"] = (
            aws_sdk_mturk.types.review_report.deserialize_aws_json_1_1(
                data["HITReviewReport"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
