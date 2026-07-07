"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DescribeAccountAssignmentDeletionStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.instance_arn
    import aws_sdk_sso_admin.types.uu_id


class DescribeAccountAssignmentDeletionStatusRequest(TypedDict, closed=True):
    instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
    r"""<p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    account_assignment_deletion_request_id: "aws_sdk_sso_admin.types.uu_id.UUId"
    """<p>The identifier that is used to track the request operation progress.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeAccountAssignmentDeletionStatusRequest,
) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["AccountAssignmentDeletionRequestId"] = value[
        "account_assignment_deletion_request_id"
    ]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeAccountAssignmentDeletionStatusRequest:
    out: DescribeAccountAssignmentDeletionStatusRequest = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError(
            "DescribeAccountAssignmentDeletionStatusRequest.instance_arn required"
        )
    if "AccountAssignmentDeletionRequestId" in data:
        out["account_assignment_deletion_request_id"] = data[
            "AccountAssignmentDeletionRequestId"
        ]
    else:
        raise DeserializationError(
            "DescribeAccountAssignmentDeletionStatusRequest.account_assignment_deletion_request_id required"
        )
    return out
