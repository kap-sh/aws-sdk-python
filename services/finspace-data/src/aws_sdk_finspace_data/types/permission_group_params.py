"""Generated from Smithy shape ``com.amazonaws.finspacedata#PermissionGroupParams``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.permission_group_id
    import aws_sdk_finspace_data.types.resource_permissions_list


class PermissionGroupParams(TypedDict, closed=True):
    permission_group_id: NotRequired[
        "aws_sdk_finspace_data.types.permission_group_id.PermissionGroupId"
    ]
    """<p>The unique identifier for the <code>PermissionGroup</code>.</p>"""
    dataset_permissions: NotRequired[
        "aws_sdk_finspace_data.types.resource_permissions_list.ResourcePermissionsList"
    ]
    """<p>List of resource permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionGroupParams) -> dict:
    out: dict = {}
    if "permission_group_id" in value:
        out["permissionGroupId"] = value["permission_group_id"]
    if "dataset_permissions" in value:
        import aws_sdk_finspace_data.types.resource_permissions_list

        out["datasetPermissions"] = (
            aws_sdk_finspace_data.types.resource_permissions_list.serialize_json(
                value["dataset_permissions"]
            )
        )
    return out


def deserialize_json(data: dict) -> PermissionGroupParams:
    out: PermissionGroupParams = {}  # type: ignore[typeddict-item]
    if "permissionGroupId" in data:
        out["permission_group_id"] = data["permissionGroupId"]
    if "datasetPermissions" in data:
        import aws_sdk_finspace_data.types.resource_permissions_list

        out["dataset_permissions"] = (
            aws_sdk_finspace_data.types.resource_permissions_list.deserialize_json(
                data["datasetPermissions"]
            )
        )
    return out
