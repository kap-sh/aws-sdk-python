"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListPermissionSetProvisioningStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.permission_set_provisioning_status_list
    import capo_sso_admin.types.token


class ListPermissionSetProvisioningStatusResponse(TypedDict, closed=True):
    permission_sets_provisioning_status: NotRequired[
        "capo_sso_admin.types.permission_set_provisioning_status_list.PermissionSetProvisioningStatusList"
    ]
    """<p>The status object for the permission set provisioning operation.</p>"""
    next_token: NotRequired["capo_sso_admin.types.token.Token"]
    """<p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPermissionSetProvisioningStatusResponse) -> dict:
    out: dict = {}
    if "permission_sets_provisioning_status" in value:
        import capo_sso_admin.types.permission_set_provisioning_status_list

        out["PermissionSetsProvisioningStatus"] = (
            capo_sso_admin.types.permission_set_provisioning_status_list.serialize_aws_json_1_1(
                value["permission_sets_provisioning_status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPermissionSetProvisioningStatusResponse:
    out: ListPermissionSetProvisioningStatusResponse = {}  # type: ignore[typeddict-item]
    if "PermissionSetsProvisioningStatus" in data:
        import capo_sso_admin.types.permission_set_provisioning_status_list

        out["permission_sets_provisioning_status"] = (
            capo_sso_admin.types.permission_set_provisioning_status_list.deserialize_aws_json_1_1(
                data["PermissionSetsProvisioningStatus"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
