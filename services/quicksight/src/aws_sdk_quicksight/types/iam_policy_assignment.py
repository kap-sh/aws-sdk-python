"""Generated from Smithy shape ``com.amazonaws.quicksight#IAMPolicyAssignment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.assignment_status
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.iam_policy_assignment_name
    import aws_sdk_quicksight.types.identity_map
    import aws_sdk_quicksight.types.string


class IAMPolicyAssignment(TypedDict, closed=True):
    aws_account_id: NotRequired["aws_sdk_quicksight.types.aws_account_id.AwsAccountId"]
    """<p>The Amazon Web Services account ID.</p>"""
    assignment_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>Assignment ID.</p>"""
    assignment_name: NotRequired[
        "aws_sdk_quicksight.types.iam_policy_assignment_name.IAMPolicyAssignmentName"
    ]
    """<p>Assignment name.</p>"""
    policy_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the IAM policy.</p>"""
    identities: NotRequired["aws_sdk_quicksight.types.identity_map.IdentityMap"]
    """<p>Identities.</p>"""
    assignment_status: NotRequired[
        "aws_sdk_quicksight.types.assignment_status.AssignmentStatus"
    ]
    """<p>Assignment status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IAMPolicyAssignment) -> dict:
    out: dict = {}
    if "aws_account_id" in value:
        out["AwsAccountId"] = value["aws_account_id"]
    if "assignment_id" in value:
        out["AssignmentId"] = value["assignment_id"]
    if "assignment_name" in value:
        out["AssignmentName"] = value["assignment_name"]
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
    return out


def deserialize_json(data: dict) -> IAMPolicyAssignment:
    out: IAMPolicyAssignment = {}  # type: ignore[typeddict-item]
    if "AwsAccountId" in data:
        out["aws_account_id"] = data["AwsAccountId"]
    if "AssignmentId" in data:
        out["assignment_id"] = data["AssignmentId"]
    if "AssignmentName" in data:
        out["assignment_name"] = data["AssignmentName"]
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
    return out
