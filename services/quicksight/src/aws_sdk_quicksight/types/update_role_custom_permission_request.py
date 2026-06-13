"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateRoleCustomPermissionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.namespace
    import aws_sdk_quicksight.types.role
    import aws_sdk_quicksight.types.role_name


class UpdateRoleCustomPermissionRequest(TypedDict):
    custom_permissions_name: "aws_sdk_quicksight.types.role_name.RoleName"
    """<p>The name of the custom permission that you want to update the role with.</p>"""
    role: "aws_sdk_quicksight.types.role.Role"
    """<p>The name of role tht you want to update.</p>"""
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that you want to create a group in. The Amazon Web Services account ID that you provide must be the same Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The namespace that contains the role that you want to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRoleCustomPermissionRequest) -> dict:
    out: dict = {}
    out["CustomPermissionsName"] = value["custom_permissions_name"]
    return out


def deserialize_json(data: dict) -> UpdateRoleCustomPermissionRequest:
    out: UpdateRoleCustomPermissionRequest = {}  # type: ignore[typeddict-item]
    if "CustomPermissionsName" in data:
        out["custom_permissions_name"] = data["CustomPermissionsName"]
    else:
        raise DeserializationError(
            "UpdateRoleCustomPermissionRequest.custom_permissions_name required"
        )
    return out
