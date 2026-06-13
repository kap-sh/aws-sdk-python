"""Generated from Smithy shape ``com.amazonaws.quicksight#ActiveIAMPolicyAssignment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.iam_policy_assignment_name


class ActiveIAMPolicyAssignment(TypedDict):
    assignment_name: NotRequired[
        "aws_sdk_quicksight.types.iam_policy_assignment_name.IAMPolicyAssignmentName"
    ]
    """<p>A name for the IAM policy assignment.</p>"""
    policy_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActiveIAMPolicyAssignment) -> dict:
    out: dict = {}
    if "assignment_name" in value:
        out["AssignmentName"] = value["assignment_name"]
    if "policy_arn" in value:
        out["PolicyArn"] = value["policy_arn"]
    return out


def deserialize_json(data: dict) -> ActiveIAMPolicyAssignment:
    out: ActiveIAMPolicyAssignment = {}  # type: ignore[typeddict-item]
    if "AssignmentName" in data:
        out["assignment_name"] = data["AssignmentName"]
    if "PolicyArn" in data:
        out["policy_arn"] = data["PolicyArn"]
    return out
