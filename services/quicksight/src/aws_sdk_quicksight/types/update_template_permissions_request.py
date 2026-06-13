"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateTemplatePermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.update_resource_permission_list


class UpdateTemplatePermissionsRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the template.</p>"""
    template_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID for the template.</p>"""
    grant_permissions: NotRequired[
        "aws_sdk_quicksight.types.update_resource_permission_list.UpdateResourcePermissionList"
    ]
    """<p>A list of resource permissions to be granted on the template. </p>"""
    revoke_permissions: NotRequired[
        "aws_sdk_quicksight.types.update_resource_permission_list.UpdateResourcePermissionList"
    ]
    """<p>A list of resource permissions to be revoked from the template. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTemplatePermissionsRequest) -> dict:
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
    return out


def deserialize_json(data: dict) -> UpdateTemplatePermissionsRequest:
    out: UpdateTemplatePermissionsRequest = {}  # type: ignore[typeddict-item]
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
    return out
