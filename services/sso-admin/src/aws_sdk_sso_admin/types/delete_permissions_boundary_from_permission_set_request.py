"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DeletePermissionsBoundaryFromPermissionSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.instance_arn
    import aws_sdk_sso_admin.types.permission_set_arn


class DeletePermissionsBoundaryFromPermissionSetRequest(TypedDict):
    instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the IAM Identity Center instance under which the operation will be executed. </p>"""
    permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn"
    """<p>The ARN of the <code>PermissionSet</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DeletePermissionsBoundaryFromPermissionSetRequest,
) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["PermissionSetArn"] = value["permission_set_arn"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeletePermissionsBoundaryFromPermissionSetRequest:
    out: DeletePermissionsBoundaryFromPermissionSetRequest = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError(
            "DeletePermissionsBoundaryFromPermissionSetRequest.instance_arn required"
        )
    if "PermissionSetArn" in data:
        out["permission_set_arn"] = data["PermissionSetArn"]
    else:
        raise DeserializationError(
            "DeletePermissionsBoundaryFromPermissionSetRequest.permission_set_arn required"
        )
    return out
