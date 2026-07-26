"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateSpacePermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.public_space_id
    import capo_quicksight.types.resource_permission_list


class UpdateSpacePermissionsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the space.</p>"""
    space_id: "capo_quicksight.types.public_space_id.PublicSpaceId"
    """<p>The ID of the space that you want to update permissions for.</p>"""
    grant_permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The permissions that you want to grant on the space.</p>"""
    revoke_permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The permissions that you want to revoke from the space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSpacePermissionsRequest) -> dict:
    out: dict = {}
    if "grant_permissions" in value:
        import capo_quicksight.types.resource_permission_list

        out["GrantPermissions"] = (
            capo_quicksight.types.resource_permission_list.serialize_json(
                value["grant_permissions"]
            )
        )
    if "revoke_permissions" in value:
        import capo_quicksight.types.resource_permission_list

        out["RevokePermissions"] = (
            capo_quicksight.types.resource_permission_list.serialize_json(
                value["revoke_permissions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSpacePermissionsRequest:
    out: UpdateSpacePermissionsRequest = {}  # type: ignore[typeddict-item]
    if "GrantPermissions" in data:
        import capo_quicksight.types.resource_permission_list

        out["grant_permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["GrantPermissions"]
            )
        )
    if "RevokePermissions" in data:
        import capo_quicksight.types.resource_permission_list

        out["revoke_permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["RevokePermissions"]
            )
        )
    return out
