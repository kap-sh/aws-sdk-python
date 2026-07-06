"""Generated from Smithy shape ``com.amazonaws.quicksight#IAMPolicyAssignmentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.assignment_status
    import aws_sdk_quicksight.types.iam_policy_assignment_name


class IAMPolicyAssignmentSummary(TypedDict, closed=True):
    assignment_name: NotRequired[
        "aws_sdk_quicksight.types.iam_policy_assignment_name.IAMPolicyAssignmentName"
    ]
    """<p>Assignment name.</p>"""
    assignment_status: NotRequired[
        "aws_sdk_quicksight.types.assignment_status.AssignmentStatus"
    ]
    """<p>Assignment status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IAMPolicyAssignmentSummary) -> dict:
    out: dict = {}
    if "assignment_name" in value:
        out["AssignmentName"] = value["assignment_name"]
    if "assignment_status" in value:
        import aws_sdk_quicksight.types.assignment_status

        out["AssignmentStatus"] = (
            aws_sdk_quicksight.types.assignment_status.serialize_json(
                value["assignment_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> IAMPolicyAssignmentSummary:
    out: IAMPolicyAssignmentSummary = {}  # type: ignore[typeddict-item]
    if "AssignmentName" in data:
        out["assignment_name"] = data["AssignmentName"]
    if "AssignmentStatus" in data:
        import aws_sdk_quicksight.types.assignment_status

        out["assignment_status"] = (
            aws_sdk_quicksight.types.assignment_status.deserialize_json(
                data["AssignmentStatus"]
            )
        )
    return out
