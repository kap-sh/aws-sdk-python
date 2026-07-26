"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupingStatusesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups.types.grouping_statuses_item

GroupingStatusesList: TypeAlias = list[
    "capo_resource_groups.types.grouping_statuses_item.GroupingStatusesItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupingStatusesList) -> list:
    import capo_resource_groups.types.grouping_statuses_item

    out: list = []
    for item in value:
        out.append(
            capo_resource_groups.types.grouping_statuses_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GroupingStatusesList:
    import capo_resource_groups.types.grouping_statuses_item

    out: GroupingStatusesList = []
    for item in data:
        out.append(
            capo_resource_groups.types.grouping_statuses_item.deserialize_json(item)
        )
    return out
