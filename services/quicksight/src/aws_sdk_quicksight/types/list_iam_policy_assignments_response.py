"""Generated from Smithy shape ``com.amazonaws.quicksight#ListIAMPolicyAssignmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.iam_policy_assignment_summary_list
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class ListIAMPolicyAssignmentsResponse(TypedDict, closed=True):
    iam_policy_assignments: NotRequired[
        "aws_sdk_quicksight.types.iam_policy_assignment_summary_list.IAMPolicyAssignmentSummaryList"
    ]
    """<p>Information describing the IAM policy assignments.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIAMPolicyAssignmentsResponse) -> dict:
    out: dict = {}
    if "iam_policy_assignments" in value:
        import aws_sdk_quicksight.types.iam_policy_assignment_summary_list

        out["IAMPolicyAssignments"] = (
            aws_sdk_quicksight.types.iam_policy_assignment_summary_list.serialize_json(
                value["iam_policy_assignments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListIAMPolicyAssignmentsResponse:
    out: ListIAMPolicyAssignmentsResponse = {}  # type: ignore[typeddict-item]
    if "IAMPolicyAssignments" in data:
        import aws_sdk_quicksight.types.iam_policy_assignment_summary_list

        out["iam_policy_assignments"] = (
            aws_sdk_quicksight.types.iam_policy_assignment_summary_list.deserialize_json(
                data["IAMPolicyAssignments"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
