"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteIAMPolicyAssignmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.iam_policy_assignment_name
    import capo_quicksight.types.namespace


class DeleteIAMPolicyAssignmentRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID where you want to delete the IAM policy assignment.</p>"""
    assignment_name: (
        "capo_quicksight.types.iam_policy_assignment_name.IAMPolicyAssignmentName"
    )
    """<p>The name of the assignment. </p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The namespace that contains the assignment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIAMPolicyAssignmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIAMPolicyAssignmentRequest:
    out: DeleteIAMPolicyAssignmentRequest = {}  # type: ignore[typeddict-item]
    return out
