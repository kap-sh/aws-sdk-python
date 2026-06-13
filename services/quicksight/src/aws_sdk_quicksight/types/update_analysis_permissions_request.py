"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAnalysisPermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.update_resource_permission_list


class UpdateAnalysisPermissionsRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the analysis whose permissions you're updating. You must be using the Amazon Web Services account that the analysis is in.</p>"""
    analysis_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the analysis whose permissions you're updating. The ID is part of the analysis URL.</p>"""
    grant_permissions: NotRequired[
        "aws_sdk_quicksight.types.update_resource_permission_list.UpdateResourcePermissionList"
    ]
    """<p>A structure that describes the permissions to add and the principal to add them to.</p>"""
    revoke_permissions: NotRequired[
        "aws_sdk_quicksight.types.update_resource_permission_list.UpdateResourcePermissionList"
    ]
    """<p>A structure that describes the permissions to remove and the principal to remove them from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAnalysisPermissionsRequest) -> dict:
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


def deserialize_json(data: dict) -> UpdateAnalysisPermissionsRequest:
    out: UpdateAnalysisPermissionsRequest = {}  # type: ignore[typeddict-item]
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
