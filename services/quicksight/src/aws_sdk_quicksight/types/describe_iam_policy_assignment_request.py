"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeIAMPolicyAssignmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.iam_policy_assignment_name
    import aws_sdk_quicksight.types.namespace


class DescribeIAMPolicyAssignmentRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the assignment that you want to describe.</p>"""
    assignment_name: (
        "aws_sdk_quicksight.types.iam_policy_assignment_name.IAMPolicyAssignmentName"
    )
    """<p>The name of the assignment, also called a rule.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The namespace that contains the assignment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeIAMPolicyAssignmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeIAMPolicyAssignmentRequest:
    out: DescribeIAMPolicyAssignmentRequest = {}  # type: ignore[typeddict-item]
    return out
