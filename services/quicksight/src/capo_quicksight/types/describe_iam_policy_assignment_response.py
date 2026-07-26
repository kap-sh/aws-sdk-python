"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeIAMPolicyAssignmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.iam_policy_assignment
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DescribeIAMPolicyAssignmentResponse(TypedDict, closed=True):
    iam_policy_assignment: NotRequired[
        "capo_quicksight.types.iam_policy_assignment.IAMPolicyAssignment"
    ]
    """<p>Information describing the IAM policy assignment.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeIAMPolicyAssignmentResponse) -> dict:
    out: dict = {}
    if "iam_policy_assignment" in value:
        import capo_quicksight.types.iam_policy_assignment

        out["IAMPolicyAssignment"] = (
            capo_quicksight.types.iam_policy_assignment.serialize_json(
                value["iam_policy_assignment"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeIAMPolicyAssignmentResponse:
    out: DescribeIAMPolicyAssignmentResponse = {}  # type: ignore[typeddict-item]
    if "IAMPolicyAssignment" in data:
        import capo_quicksight.types.iam_policy_assignment

        out["iam_policy_assignment"] = (
            capo_quicksight.types.iam_policy_assignment.deserialize_json(
                data["IAMPolicyAssignment"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
