"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateIAMPolicyAssignmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.assignment_status
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.iam_policy_assignment_name
    import aws_sdk_quicksight.types.identity_map
    import aws_sdk_quicksight.types.namespace


class CreateIAMPolicyAssignmentRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account where you want to assign an IAM policy to Amazon Quick Sight users or groups.</p>"""
    assignment_name: (
        "aws_sdk_quicksight.types.iam_policy_assignment_name.IAMPolicyAssignmentName"
    )
    """<p>The name of the assignment, also called a rule. The name must be unique within the Amazon Web Services account.</p>"""
    assignment_status: "aws_sdk_quicksight.types.assignment_status.AssignmentStatus"
    """<p>The status of the assignment. Possible values are as follows:</p> <ul> <li> <p> <code>ENABLED</code> - Anything specified in this assignment is used when creating the data source.</p> </li> <li> <p> <code>DISABLED</code> - This assignment isn't used when creating the data source.</p> </li> <li> <p> <code>DRAFT</code> - This assignment is an unfinished draft and isn't used when creating the data source.</p> </li> </ul>"""
    policy_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The ARN for the IAM policy to apply to the Amazon Quick Sight users and groups specified in this assignment.</p>"""
    identities: NotRequired["aws_sdk_quicksight.types.identity_map.IdentityMap"]
    """<p>The Amazon Quick Sight users, groups, or both that you want to assign the policy to.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The namespace that contains the assignment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIAMPolicyAssignmentRequest) -> dict:
    out: dict = {}
    out["AssignmentName"] = value["assignment_name"]
    import aws_sdk_quicksight.types.assignment_status

    out["AssignmentStatus"] = aws_sdk_quicksight.types.assignment_status.serialize_json(
        value["assignment_status"]
    )
    if "policy_arn" in value:
        out["PolicyArn"] = value["policy_arn"]
    if "identities" in value:
        import aws_sdk_quicksight.types.identity_map

        out["Identities"] = aws_sdk_quicksight.types.identity_map.serialize_json(
            value["identities"]
        )
    return out


def deserialize_json(data: dict) -> CreateIAMPolicyAssignmentRequest:
    out: CreateIAMPolicyAssignmentRequest = {}  # type: ignore[typeddict-item]
    if "AssignmentName" in data:
        out["assignment_name"] = data["AssignmentName"]
    else:
        raise DeserializationError(
            "CreateIAMPolicyAssignmentRequest.assignment_name required"
        )
    if "AssignmentStatus" in data:
        import aws_sdk_quicksight.types.assignment_status

        out["assignment_status"] = (
            aws_sdk_quicksight.types.assignment_status.deserialize_json(
                data["AssignmentStatus"]
            )
        )
    else:
        raise DeserializationError(
            "CreateIAMPolicyAssignmentRequest.assignment_status required"
        )
    if "PolicyArn" in data:
        out["policy_arn"] = data["PolicyArn"]
    if "Identities" in data:
        import aws_sdk_quicksight.types.identity_map

        out["identities"] = aws_sdk_quicksight.types.identity_map.deserialize_json(
            data["Identities"]
        )
    return out
