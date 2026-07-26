"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateActionConnectorPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.resource_permission_list
    import capo_quicksight.types.short_restrictive_resource_id


class UpdateActionConnectorPermissionsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID that contains the action connector.</p>"""
    action_connector_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The unique identifier of the action connector whose permissions you want to update.</p>"""
    grant_permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The permissions to grant to users and groups for this action connector.</p>"""
    revoke_permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The permissions to revoke from users and groups for this action connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateActionConnectorPermissionsRequest) -> dict:
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


def deserialize_json(data: dict) -> UpdateActionConnectorPermissionsRequest:
    out: UpdateActionConnectorPermissionsRequest = {}  # type: ignore[typeddict-item]
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
