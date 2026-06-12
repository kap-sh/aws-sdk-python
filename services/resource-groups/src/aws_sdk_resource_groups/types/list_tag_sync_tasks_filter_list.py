"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ListTagSyncTasksFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.list_tag_sync_tasks_filter

ListTagSyncTasksFilterList: TypeAlias = list[
    "aws_sdk_resource_groups.types.list_tag_sync_tasks_filter.ListTagSyncTasksFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListTagSyncTasksFilterList) -> list:
    import aws_sdk_resource_groups.types.list_tag_sync_tasks_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resource_groups.types.list_tag_sync_tasks_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListTagSyncTasksFilterList:
    import aws_sdk_resource_groups.types.list_tag_sync_tasks_filter

    out: ListTagSyncTasksFilterList = []
    for item in data:
        out.append(
            aws_sdk_resource_groups.types.list_tag_sync_tasks_filter.deserialize_json(
                item
            )
        )
    return out
