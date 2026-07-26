"""Generated from Smithy shape ``com.amazonaws.resourcegroups#StartTagSyncTaskOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.group_arn_v2
    import capo_resource_groups.types.group_name
    import capo_resource_groups.types.resource_query
    import capo_resource_groups.types.role_arn
    import capo_resource_groups.types.tag_key
    import capo_resource_groups.types.tag_sync_task_arn
    import capo_resource_groups.types.tag_value


class StartTagSyncTaskOutput(TypedDict, closed=True):
    group_arn: NotRequired["capo_resource_groups.types.group_arn_v2.GroupArnV2"]
    """<p>The Amazon resource name (ARN) of the application group for which you want to add or remove resources. </p>"""
    group_name: NotRequired["capo_resource_groups.types.group_name.GroupName"]
    """<p>The name of the application group to onboard and sync resources.</p>"""
    task_arn: NotRequired["capo_resource_groups.types.tag_sync_task_arn.TagSyncTaskArn"]
    """<p>The Amazon resource name (ARN) of the new tag-sync task. </p>"""
    tag_key: NotRequired["capo_resource_groups.types.tag_key.TagKey"]
    """<p>The tag key of the tag-sync task. </p>"""
    tag_value: NotRequired["capo_resource_groups.types.tag_value.TagValue"]
    """<p>The tag value of the tag-sync task. </p>"""
    resource_query: NotRequired[
        "capo_resource_groups.types.resource_query.ResourceQuery"
    ]
    role_arn: NotRequired["capo_resource_groups.types.role_arn.RoleArn"]
    """<p>The Amazon resource name (ARN) of the role assumed by the service to tag and untag resources on your behalf.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTagSyncTaskOutput) -> dict:
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
        import capo_resource_groups.types.resource_query

        out["ResourceQuery"] = capo_resource_groups.types.resource_query.serialize_json(
            value["resource_query"]
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> StartTagSyncTaskOutput:
    out: StartTagSyncTaskOutput = {}  # type: ignore[typeddict-item]
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
        import capo_resource_groups.types.resource_query

        out["resource_query"] = (
            capo_resource_groups.types.resource_query.deserialize_json(
                data["ResourceQuery"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
