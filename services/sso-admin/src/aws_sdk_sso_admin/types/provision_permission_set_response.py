"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ProvisionPermissionSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.permission_set_provisioning_status


class ProvisionPermissionSetResponse(TypedDict):
    permission_set_provisioning_status: NotRequired[
        "aws_sdk_sso_admin.types.permission_set_provisioning_status.PermissionSetProvisioningStatus"
    ]
    """<p>The status object for the permission set provisioning operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionPermissionSetResponse) -> dict:
    out: dict = {}
    if "permission_set_provisioning_status" in value:
        import aws_sdk_sso_admin.types.permission_set_provisioning_status

        out["PermissionSetProvisioningStatus"] = (
            aws_sdk_sso_admin.types.permission_set_provisioning_status.serialize_aws_json_1_1(
                value["permission_set_provisioning_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisionPermissionSetResponse:
    out: ProvisionPermissionSetResponse = {}  # type: ignore[typeddict-item]
    if "PermissionSetProvisioningStatus" in data:
        import aws_sdk_sso_admin.types.permission_set_provisioning_status

        out["permission_set_provisioning_status"] = (
            aws_sdk_sso_admin.types.permission_set_provisioning_status.deserialize_aws_json_1_1(
                data["PermissionSetProvisioningStatus"]
            )
        )
    return out
