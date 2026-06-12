"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ListGroupingStatusesFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.list_grouping_statuses_filter_value

ListGroupingStatusesFilterValues: TypeAlias = list[
    "aws_sdk_resource_groups.types.list_grouping_statuses_filter_value.ListGroupingStatusesFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupingStatusesFilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> ListGroupingStatusesFilterValues:
    return list(data)
