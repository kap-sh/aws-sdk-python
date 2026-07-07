"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ListGroupingStatusesFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_resource_groups.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.list_grouping_statuses_filter_name
    import aws_sdk_resource_groups.types.list_grouping_statuses_filter_values


class ListGroupingStatusesFilter(TypedDict, closed=True):
    name: "aws_sdk_resource_groups.types.list_grouping_statuses_filter_name.ListGroupingStatusesFilterName"
    """<p>The name of the filter. Filter names are case-sensitive. </p>"""
    values: "aws_sdk_resource_groups.types.list_grouping_statuses_filter_values.ListGroupingStatusesFilterValues"
    """<p>One or more filter values. Allowed filter values vary by resource filter name, and are case-sensitive. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupingStatusesFilter) -> dict:
    out: dict = {}
    import aws_sdk_resource_groups.types.list_grouping_statuses_filter_name

    out["Name"] = (
        aws_sdk_resource_groups.types.list_grouping_statuses_filter_name.serialize_json(
            value["name"]
        )
    )
    import aws_sdk_resource_groups.types.list_grouping_statuses_filter_values

    out["Values"] = (
        aws_sdk_resource_groups.types.list_grouping_statuses_filter_values.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListGroupingStatusesFilter:
    out: ListGroupingStatusesFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_resource_groups.types.list_grouping_statuses_filter_name

        out["name"] = (
            aws_sdk_resource_groups.types.list_grouping_statuses_filter_name.deserialize_json(
                data["Name"]
            )
        )
    else:
        raise DeserializationError("ListGroupingStatusesFilter.name required")
    if "Values" in data:
        import aws_sdk_resource_groups.types.list_grouping_statuses_filter_values

        out["values"] = (
            aws_sdk_resource_groups.types.list_grouping_statuses_filter_values.deserialize_json(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("ListGroupingStatusesFilter.values required")
    return out
