"""Generated from Smithy shape ``com.amazonaws.quicksight#ListIAMPolicyAssignmentsForUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.active_iam_policy_assignment_list
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class ListIAMPolicyAssignmentsForUserResponse(TypedDict, closed=True):
    active_assignments: NotRequired[
        "aws_sdk_quicksight.types.active_iam_policy_assignment_list.ActiveIAMPolicyAssignmentList"
    ]
    """<p>The active assignments for this user.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIAMPolicyAssignmentsForUserResponse) -> dict:
    out: dict = {}
    if "active_assignments" in value:
        import aws_sdk_quicksight.types.active_iam_policy_assignment_list

        out["ActiveAssignments"] = (
            aws_sdk_quicksight.types.active_iam_policy_assignment_list.serialize_json(
                value["active_assignments"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIAMPolicyAssignmentsForUserResponse:
    out: ListIAMPolicyAssignmentsForUserResponse = {}  # type: ignore[typeddict-item]
    if "ActiveAssignments" in data:
        import aws_sdk_quicksight.types.active_iam_policy_assignment_list

        out["active_assignments"] = (
            aws_sdk_quicksight.types.active_iam_policy_assignment_list.deserialize_json(
                data["ActiveAssignments"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
