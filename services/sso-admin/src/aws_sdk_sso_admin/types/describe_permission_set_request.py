"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DescribePermissionSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.instance_arn
    import aws_sdk_sso_admin.types.permission_set_arn


class DescribePermissionSetRequest(TypedDict, closed=True):
    instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
    r"""<p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn"
    """<p>The ARN of the permission set. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePermissionSetRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["PermissionSetArn"] = value["permission_set_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePermissionSetRequest:
    out: DescribePermissionSetRequest = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError("DescribePermissionSetRequest.instance_arn required")
    if "PermissionSetArn" in data:
        out["permission_set_arn"] = data["PermissionSetArn"]
    else:
        raise DeserializationError(
            "DescribePermissionSetRequest.permission_set_arn required"
        )
    return out
