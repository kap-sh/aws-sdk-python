"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListPermissionSetProvisioningStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.permission_set_provisioning_status_list
    import aws_sdk_sso_admin.types.token


class ListPermissionSetProvisioningStatusResponse(TypedDict):
    permission_sets_provisioning_status: NotRequired[
        "aws_sdk_sso_admin.types.permission_set_provisioning_status_list.PermissionSetProvisioningStatusList"
    ]
    """<p>The status object for the permission set provisioning operation.</p>"""
    next_token: NotRequired["aws_sdk_sso_admin.types.token.Token"]
    """<p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPermissionSetProvisioningStatusResponse) -> dict:
    out: dict = {}
    if "permission_sets_provisioning_status" in value:
        import aws_sdk_sso_admin.types.permission_set_provisioning_status_list

        out["PermissionSetsProvisioningStatus"] = (
            aws_sdk_sso_admin.types.permission_set_provisioning_status_list.serialize_aws_json_1_1(
                value["permission_sets_provisioning_status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPermissionSetProvisioningStatusResponse:
    out: ListPermissionSetProvisioningStatusResponse = {}  # type: ignore[typeddict-item]
    if "PermissionSetsProvisioningStatus" in data:
        import aws_sdk_sso_admin.types.permission_set_provisioning_status_list

        out["permission_sets_provisioning_status"] = (
            aws_sdk_sso_admin.types.permission_set_provisioning_status_list.deserialize_aws_json_1_1(
                data["PermissionSetsProvisioningStatus"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
