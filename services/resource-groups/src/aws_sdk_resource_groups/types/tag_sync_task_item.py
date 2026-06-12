"""Generated from Smithy shape ``com.amazonaws.resourcegroups#TagSyncTaskItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.error_message
    import aws_sdk_resource_groups.types.group_arn_v2
    import aws_sdk_resource_groups.types.group_name
    import aws_sdk_resource_groups.types.resource_query
    import aws_sdk_resource_groups.types.role_arn
    import aws_sdk_resource_groups.types.tag_key
    import aws_sdk_resource_groups.types.tag_sync_task_arn
    import aws_sdk_resource_groups.types.tag_sync_task_status
    import aws_sdk_resource_groups.types.tag_value
    import aws_sdk_resource_groups.types.timestamp


class TagSyncTaskItem(TypedDict):
    group_arn: NotRequired["aws_sdk_resource_groups.types.group_arn_v2.GroupArnV2"]
    """<p>The Amazon resource name (ARN) of the application group. </p>"""
    group_name: NotRequired["aws_sdk_resource_groups.types.group_name.GroupName"]
    """<p>The name of the application group. </p>"""
    task_arn: NotRequired[
        "aws_sdk_resource_groups.types.tag_sync_task_arn.TagSyncTaskArn"
    ]
    """<p>The Amazon resource name (ARN) of the tag-sync task. </p>"""
    tag_key: NotRequired["aws_sdk_resource_groups.types.tag_key.TagKey"]
    """<p>The tag key. </p>"""
    tag_value: NotRequired["aws_sdk_resource_groups.types.tag_value.TagValue"]
    """<p>The tag value. </p>"""
    resource_query: NotRequired[
        "aws_sdk_resource_groups.types.resource_query.ResourceQuery"
    ]
    role_arn: NotRequired["aws_sdk_resource_groups.types.role_arn.RoleArn"]
    """<p>The Amazon resource name (ARN) of the role assumed by the service to tag and untag resources on your behalf.</p>"""
    status: NotRequired[
        "aws_sdk_resource_groups.types.tag_sync_task_status.TagSyncTaskStatus"
    ]
    """<p>The status of the tag-sync task. </p> <p>Valid values include:</p> <ul> <li> <p> <code>ACTIVE</code> - The tag-sync task is actively managing resources in the application by adding or removing the <code>awsApplication</code> tag from resources when they are tagged or untagged with the specified tag key-value pair. </p> </li> <li> <p> <code>ERROR</code> - The tag-sync task is not actively managing resources in the application. Review the <code>ErrorMessage</code> for more information about resolving the error. </p> </li> </ul>"""
    error_message: NotRequired[
        "aws_sdk_resource_groups.types.error_message.ErrorMessage"
    ]
    """<p>The specific error message in cases where the tag-sync task status is <code>Error</code>.</p>"""
    created_at: NotRequired["aws_sdk_resource_groups.types.timestamp.timestamp"]
    """<p>The timestamp of when the tag-sync task was created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagSyncTaskItem) -> dict:
    out: dict = {}
    if "group_arn" in value:
        out["GroupArn"] = value["group_arn"]
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    if "tag_key" in value:
        out["TagKey"] = value["tag_key"]
    if "tag_value" in value:
        out["TagValue"] = value["tag_value"]
    if "resource_query" in value:
        import aws_sdk_resource_groups.types.resource_query

        out["ResourceQuery"] = (
            aws_sdk_resource_groups.types.resource_query.serialize_json(
                value["resource_query"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "status" in value:
        import aws_sdk_resource_groups.types.tag_sync_task_status

        out["Status"] = (
            aws_sdk_resource_groups.types.tag_sync_task_status.serialize_json(
                value["status"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "created_at" in value:
        import aws_sdk_resource_groups.types.timestamp

        out["CreatedAt"] = aws_sdk_resource_groups.types.timestamp.serialize_json(
            value["created_at"]
        )
    return out


def deserialize_json(data: dict) -> TagSyncTaskItem:
    out: TagSyncTaskItem = {}  # type: ignore[typeddict-item]
    if "GroupArn" in data:
        out["group_arn"] = data["GroupArn"]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "TaskArn" in data:
        out["task_arn"] = data["TaskArn"]
    if "TagKey" in data:
        out["tag_key"] = data["TagKey"]
    if "TagValue" in data:
        out["tag_value"] = data["TagValue"]
    if "ResourceQuery" in data:
        import aws_sdk_resource_groups.types.resource_query

        out["resource_query"] = (
            aws_sdk_resource_groups.types.resource_query.deserialize_json(
                data["ResourceQuery"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Status" in data:
        import aws_sdk_resource_groups.types.tag_sync_task_status

        out["status"] = (
            aws_sdk_resource_groups.types.tag_sync_task_status.deserialize_json(
                data["Status"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "CreatedAt" in data:
        import aws_sdk_resource_groups.types.timestamp

        out["created_at"] = aws_sdk_resource_groups.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    return out
