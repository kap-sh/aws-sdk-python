"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ListTagSyncTasksOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.next_token
    import capo_resource_groups.types.tag_sync_task_list


class ListTagSyncTasksOutput(TypedDict, closed=True):
    tag_sync_tasks: NotRequired[
        "capo_resource_groups.types.tag_sync_task_list.TagSyncTaskList"
    ]
    """<p>A list of tag-sync tasks and information about each task. </p>"""
    next_token: NotRequired["capo_resource_groups.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagSyncTasksOutput) -> dict:
    out: dict = {}
    if "tag_sync_tasks" in value:
        import capo_resource_groups.types.tag_sync_task_list

        out["TagSyncTasks"] = (
            capo_resource_groups.types.tag_sync_task_list.serialize_json(
                value["tag_sync_tasks"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTagSyncTasksOutput:
    out: ListTagSyncTasksOutput = {}  # type: ignore[typeddict-item]
    if "TagSyncTasks" in data:
        import capo_resource_groups.types.tag_sync_task_list

        out["tag_sync_tasks"] = (
            capo_resource_groups.types.tag_sync_task_list.deserialize_json(
                data["TagSyncTasks"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
