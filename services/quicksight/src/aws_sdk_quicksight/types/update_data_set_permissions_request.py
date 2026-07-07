"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateDataSetPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.resource_id
    import aws_sdk_quicksight.types.resource_permission_list


class UpdateDataSetPermissionsRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    data_set_id: "aws_sdk_quicksight.types.resource_id.ResourceId"
    """<p>The ID for the dataset whose permissions you want to update. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    grant_permissions: NotRequired[
        "aws_sdk_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The resource permissions that you want to grant to the dataset.</p>"""
    revoke_permissions: NotRequired[
        "aws_sdk_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The resource permissions that you want to revoke from the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataSetPermissionsRequest) -> dict:
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


def deserialize_json(data: dict) -> UpdateDataSetPermissionsRequest:
    out: UpdateDataSetPermissionsRequest = {}  # type: ignore[typeddict-item]
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
