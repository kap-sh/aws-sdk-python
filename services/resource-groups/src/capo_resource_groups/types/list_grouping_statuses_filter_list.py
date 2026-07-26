"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ListGroupingStatusesFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups.types.list_grouping_statuses_filter

ListGroupingStatusesFilterList: TypeAlias = list[
    "capo_resource_groups.types.list_grouping_statuses_filter.ListGroupingStatusesFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupingStatusesFilterList) -> list:
    import capo_resource_groups.types.list_grouping_statuses_filter

    out: list = []
    for item in value:
        out.append(
            capo_resource_groups.types.list_grouping_statuses_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListGroupingStatusesFilterList:
    import capo_resource_groups.types.list_grouping_statuses_filter

    out: ListGroupingStatusesFilterList = []
    for item in data:
        out.append(
            capo_resource_groups.types.list_grouping_statuses_filter.deserialize_json(
                item
            )
        )
    return out
