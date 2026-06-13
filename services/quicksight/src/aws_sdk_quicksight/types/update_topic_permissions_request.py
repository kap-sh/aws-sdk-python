"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateTopicPermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.topic_id
    import aws_sdk_quicksight.types.update_resource_permission_list


class UpdateTopicPermissionsRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the topic that you want to update the permissions for.</p>"""
    topic_id: "aws_sdk_quicksight.types.topic_id.TopicId"
    """<p>The ID of the topic that you want to modify. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    grant_permissions: NotRequired[
        "aws_sdk_quicksight.types.update_resource_permission_list.UpdateResourcePermissionList"
    ]
    """<p>The resource permissions that you want to grant to the topic.</p>"""
    revoke_permissions: NotRequired[
        "aws_sdk_quicksight.types.update_resource_permission_list.UpdateResourcePermissionList"
    ]
    """<p>The resource permissions that you want to revoke from the topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTopicPermissionsRequest) -> dict:
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


def deserialize_json(data: dict) -> UpdateTopicPermissionsRequest:
    out: UpdateTopicPermissionsRequest = {}  # type: ignore[typeddict-item]
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
