"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteIAMPolicyAssignmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.iam_policy_assignment_name
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DeleteIAMPolicyAssignmentResponse(TypedDict):
    assignment_name: NotRequired[
        "aws_sdk_quicksight.types.iam_policy_assignment_name.IAMPolicyAssignmentName"
    ]
    """<p>The name of the assignment. </p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIAMPolicyAssignmentResponse) -> dict:
    out: dict = {}
    if "assignment_name" in value:
        out["AssignmentName"] = value["assignment_name"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DeleteIAMPolicyAssignmentResponse:
    out: DeleteIAMPolicyAssignmentResponse = {}  # type: ignore[typeddict-item]
    if "AssignmentName" in data:
        out["assignment_name"] = data["AssignmentName"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
