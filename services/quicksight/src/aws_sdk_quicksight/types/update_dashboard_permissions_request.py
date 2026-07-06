"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateDashboardPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.update_link_permission_list
    import aws_sdk_quicksight.types.update_resource_permission_list


class UpdateDashboardPermissionsRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the dashboard whose permissions you're updating.</p>"""
    dashboard_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID for the dashboard.</p>"""
    grant_permissions: NotRequired[
        "aws_sdk_quicksight.types.update_resource_permission_list.UpdateResourcePermissionList"
    ]
    """<p>The permissions that you want to grant on this resource.</p>"""
    revoke_permissions: NotRequired[
        "aws_sdk_quicksight.types.update_resource_permission_list.UpdateResourcePermissionList"
    ]
    """<p>The permissions that you want to revoke from this resource.</p>"""
    grant_link_permissions: NotRequired[
        "aws_sdk_quicksight.types.update_link_permission_list.UpdateLinkPermissionList"
    ]
    """<p>Grants link permissions to all users in a defined namespace.</p>"""
    revoke_link_permissions: NotRequired[
        "aws_sdk_quicksight.types.update_link_permission_list.UpdateLinkPermissionList"
    ]
    """<p>Revokes link permissions from all users in a defined namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDashboardPermissionsRequest) -> dict:
    out: dict = {}
    if "grant_permissions" in value:
        import aws_sdk_quicksight.types.update_resource_permission_list

        out["GrantPermissions"] = (
            aws_sdk_quicksight.types.update_resource_permission_list.serialize_json(
                value["grant_permissions"]
            )
        )
    if "revoke_permissions" in value:
        import aws_sdk_quicksight.types.update_resource_permission_list

        out["RevokePermissions"] = (
            aws_sdk_quicksight.types.update_resource_permission_list.serialize_json(
                value["revoke_permissions"]
            )
        )
    if "grant_link_permissions" in value:
        import aws_sdk_quicksight.types.update_link_permission_list

        out["GrantLinkPermissions"] = (
            aws_sdk_quicksight.types.update_link_permission_list.serialize_json(
                value["grant_link_permissions"]
            )
        )
    if "revoke_link_permissions" in value:
        import aws_sdk_quicksight.types.update_link_permission_list

        out["RevokeLinkPermissions"] = (
            aws_sdk_quicksight.types.update_link_permission_list.serialize_json(
                value["revoke_link_permissions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDashboardPermissionsRequest:
    out: UpdateDashboardPermissionsRequest = {}  # type: ignore[typeddict-item]
    if "GrantPermissions" in data:
        import aws_sdk_quicksight.types.update_resource_permission_list

        out["grant_permissions"] = (
            aws_sdk_quicksight.types.update_resource_permission_list.deserialize_json(
                data["GrantPermissions"]
            )
        )
    if "RevokePermissions" in data:
        import aws_sdk_quicksight.types.update_resource_permission_list

        out["revoke_permissions"] = (
            aws_sdk_quicksight.types.update_resource_permission_list.deserialize_json(
                data["RevokePermissions"]
            )
        )
    if "GrantLinkPermissions" in data:
        import aws_sdk_quicksight.types.update_link_permission_list

        out["grant_link_permissions"] = (
            aws_sdk_quicksight.types.update_link_permission_list.deserialize_json(
                data["GrantLinkPermissions"]
            )
        )
    if "RevokeLinkPermissions" in data:
        import aws_sdk_quicksight.types.update_link_permission_list

        out["revoke_link_permissions"] = (
            aws_sdk_quicksight.types.update_link_permission_list.deserialize_json(
                data["RevokeLinkPermissions"]
            )
        )
    return out
