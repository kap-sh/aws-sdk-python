"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateActionConnectorPermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.resource_permission_list
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class UpdateActionConnectorPermissionsRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID that contains the action connector.</p>"""
    action_connector_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The unique identifier of the action connector whose permissions you want to update.</p>"""
    grant_permissions: NotRequired[
        "aws_sdk_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The permissions to grant to users and groups for this action connector.</p>"""
    revoke_permissions: NotRequired[
        "aws_sdk_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The permissions to revoke from users and groups for this action connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateActionConnectorPermissionsRequest) -> dict:
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


def deserialize_json(data: dict) -> UpdateActionConnectorPermissionsRequest:
    out: UpdateActionConnectorPermissionsRequest = {}  # type: ignore[typeddict-item]
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
