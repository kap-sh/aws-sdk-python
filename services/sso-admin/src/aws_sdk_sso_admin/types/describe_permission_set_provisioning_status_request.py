"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DescribePermissionSetProvisioningStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.instance_arn
    import aws_sdk_sso_admin.types.uu_id


class DescribePermissionSetProvisioningStatusRequest(TypedDict, closed=True):
    instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
    r"""<p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    provision_permission_set_request_id: "aws_sdk_sso_admin.types.uu_id.UUId"
    """<p>The identifier that is provided by the <a>ProvisionPermissionSet</a> call to retrieve the current status of the provisioning workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribePermissionSetProvisioningStatusRequest,
) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["ProvisionPermissionSetRequestId"] = value[
        "provision_permission_set_request_id"
    ]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribePermissionSetProvisioningStatusRequest:
    out: DescribePermissionSetProvisioningStatusRequest = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError(
            "DescribePermissionSetProvisioningStatusRequest.instance_arn required"
        )
    if "ProvisionPermissionSetRequestId" in data:
        out["provision_permission_set_request_id"] = data[
            "ProvisionPermissionSetRequestId"
        ]
    else:
        raise DeserializationError(
            "DescribePermissionSetProvisioningStatusRequest.provision_permission_set_request_id required"
        )
    return out
