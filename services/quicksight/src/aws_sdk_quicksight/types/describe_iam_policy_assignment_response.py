"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeIAMPolicyAssignmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.iam_policy_assignment
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeIAMPolicyAssignmentResponse(TypedDict):
    iam_policy_assignment: NotRequired[
        "aws_sdk_quicksight.types.iam_policy_assignment.IAMPolicyAssignment"
    ]
    """<p>Information describing the IAM policy assignment.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeIAMPolicyAssignmentResponse) -> dict:
    out: dict = {}
    if "iam_policy_assignment" in value:
        import aws_sdk_quicksight.types.iam_policy_assignment

        out["IAMPolicyAssignment"] = (
            aws_sdk_quicksight.types.iam_policy_assignment.serialize_json(
                value["iam_policy_assignment"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeIAMPolicyAssignmentResponse:
    out: DescribeIAMPolicyAssignmentResponse = {}  # type: ignore[typeddict-item]
    if "IAMPolicyAssignment" in data:
        import aws_sdk_quicksight.types.iam_policy_assignment

        out["iam_policy_assignment"] = (
            aws_sdk_quicksight.types.iam_policy_assignment.deserialize_json(
                data["IAMPolicyAssignment"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
