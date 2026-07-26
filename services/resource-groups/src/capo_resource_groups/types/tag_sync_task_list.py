"""Generated from Smithy shape ``com.amazonaws.resourcegroups#TagSyncTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups.types.tag_sync_task_item

TagSyncTaskList: TypeAlias = list[
    "capo_resource_groups.types.tag_sync_task_item.TagSyncTaskItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: TagSyncTaskList) -> list:
    import capo_resource_groups.types.tag_sync_task_item

    out: list = []
    for item in value:
        out.append(capo_resource_groups.types.tag_sync_task_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagSyncTaskList:
    import capo_resource_groups.types.tag_sync_task_item

    out: TagSyncTaskList = []
    for item in data:
        out.append(capo_resource_groups.types.tag_sync_task_item.deserialize_json(item))
    return out
