"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateIAMPolicyAssignmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.assignment_status
    import aws_sdk_quicksight.types.iam_policy_assignment_name
    import aws_sdk_quicksight.types.identity_map
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class UpdateIAMPolicyAssignmentResponse(TypedDict, closed=True):
    assignment_name: NotRequired[
        "aws_sdk_quicksight.types.iam_policy_assignment_name.IAMPolicyAssignmentName"
    ]
    """<p>The name of the assignment or rule.</p>"""
    assignment_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The ID of the assignment.</p>"""
    policy_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The ARN for the IAM policy applied to the Amazon Quick Sight users and groups specified in this assignment.</p>"""
    identities: NotRequired["aws_sdk_quicksight.types.identity_map.IdentityMap"]
    """<p>The Amazon Quick Sight users, groups, or both that the IAM policy is assigned to.</p>"""
    assignment_status: NotRequired[
        "aws_sdk_quicksight.types.assignment_status.AssignmentStatus"
    ]
    """<p>The status of the assignment. Possible values are as follows:</p> <ul> <li> <p> <code>ENABLED</code> - Anything specified in this assignment is used when creating the data source.</p> </li> <li> <p> <code>DISABLED</code> - This assignment isn't used when creating the data source.</p> </li> <li> <p> <code>DRAFT</code> - This assignment is an unfinished draft and isn't used when creating the data source.</p> </li> </ul>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIAMPolicyAssignmentResponse) -> dict:
    out: dict = {}
    if "assignment_name" in value:
        out["AssignmentName"] = value["assignment_name"]
    if "assignment_id" in value:
        out["AssignmentId"] = value["assignment_id"]
    if "policy_arn" in value:
        out["PolicyArn"] = value["policy_arn"]
    if "identities" in value:
        import aws_sdk_quicksight.types.identity_map

        out["Identities"] = aws_sdk_quicksight.types.identity_map.serialize_json(
            value["identities"]
        )
    if "assignment_status" in value:
        import aws_sdk_quicksight.types.assignment_status

        out["AssignmentStatus"] = (
            aws_sdk_quicksight.types.assignment_status.serialize_json(
                value["assignment_status"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateIAMPolicyAssignmentResponse:
    out: UpdateIAMPolicyAssignmentResponse = {}  # type: ignore[typeddict-item]
    if "AssignmentName" in data:
        out["assignment_name"] = data["AssignmentName"]
    if "AssignmentId" in data:
        out["assignment_id"] = data["AssignmentId"]
    if "PolicyArn" in data:
        out["policy_arn"] = data["PolicyArn"]
    if "Identities" in data:
        import aws_sdk_quicksight.types.identity_map

        out["identities"] = aws_sdk_quicksight.types.identity_map.deserialize_json(
            data["Identities"]
        )
    if "AssignmentStatus" in data:
        import aws_sdk_quicksight.types.assignment_status

        out["assignment_status"] = (
            aws_sdk_quicksight.types.assignment_status.deserialize_json(
                data["AssignmentStatus"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
