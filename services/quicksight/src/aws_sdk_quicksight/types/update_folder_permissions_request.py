"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateFolderPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.resource_permission_list
    import aws_sdk_quicksight.types.restrictive_resource_id


class UpdateFolderPermissionsRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that contains the folder to update.</p>"""
    folder_id: "aws_sdk_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    """<p>The ID of the folder.</p>"""
    grant_permissions: NotRequired[
        "aws_sdk_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The permissions that you want to grant on a resource. Namespace ARNs are not supported <code>Principal</code> values for folder permissions.</p>"""
    revoke_permissions: NotRequired[
        "aws_sdk_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The permissions that you want to revoke from a resource. Namespace ARNs are not supported <code>Principal</code> values for folder permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFolderPermissionsRequest) -> dict:
    out: dict = {}
    if "grant_permissions" in value:
        import aws_sdk_quicksight.types.resource_permission_list

        out["GrantPermissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.serialize_json(
                value["grant_permissions"]
            )
        )
    if "revoke_permissions" in value:
        import aws_sdk_quicksight.types.resource_permission_list

        out["RevokePermissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.serialize_json(
                value["revoke_permissions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateFolderPermissionsRequest:
    out: UpdateFolderPermissionsRequest = {}  # type: ignore[typeddict-item]
    if "GrantPermissions" in data:
        import aws_sdk_quicksight.types.resource_permission_list

        out["grant_permissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.deserialize_json(
                data["GrantPermissions"]
            )
        )
    if "RevokePermissions" in data:
        import aws_sdk_quicksight.types.resource_permission_list

        out["revoke_permissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.deserialize_json(
                data["RevokePermissions"]
            )
        )
    return out
