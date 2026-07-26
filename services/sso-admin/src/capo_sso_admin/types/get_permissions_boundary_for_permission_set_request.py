"""Generated from Smithy shape ``com.amazonaws.ssoadmin#GetPermissionsBoundaryForPermissionSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.instance_arn
    import capo_sso_admin.types.permission_set_arn


class GetPermissionsBoundaryForPermissionSetRequest(TypedDict, closed=True):
    instance_arn: "capo_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the IAM Identity Center instance under which the operation will be executed. </p>"""
    permission_set_arn: "capo_sso_admin.types.permission_set_arn.PermissionSetArn"
    """<p>The ARN of the <code>PermissionSet</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetPermissionsBoundaryForPermissionSetRequest,
) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["PermissionSetArn"] = value["permission_set_arn"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetPermissionsBoundaryForPermissionSetRequest:
    out: GetPermissionsBoundaryForPermissionSetRequest = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError(
            "GetPermissionsBoundaryForPermissionSetRequest.instance_arn required"
        )
    if "PermissionSetArn" in data:
        out["permission_set_arn"] = data["PermissionSetArn"]
    else:
        raise DeserializationError(
            "GetPermissionsBoundaryForPermissionSetRequest.permission_set_arn required"
        )
    return out
