"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ListGroupingStatusesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resource_groups.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_string_v2
    import aws_sdk_resource_groups.types.list_grouping_statuses_filter_list
    import aws_sdk_resource_groups.types.max_results
    import aws_sdk_resource_groups.types.next_token


class ListGroupingStatusesInput(TypedDict, closed=True):
    group: "aws_sdk_resource_groups.types.group_string_v2.GroupStringV2"
    """<p>The application group identifier, expressed as an Amazon resource name (ARN) or the application group name. </p>"""
    max_results: NotRequired["aws_sdk_resource_groups.types.max_results.MaxResults"]
    """<p>The maximum number of resources and their statuses returned in the response. </p>"""
    filters: NotRequired[
        "aws_sdk_resource_groups.types.list_grouping_statuses_filter_list.ListGroupingStatusesFilterList"
    ]
    """<p>The filter name and value pair that is used to return more specific results from a list of resources. </p>"""
    next_token: NotRequired["aws_sdk_resource_groups.types.next_token.NextToken"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value provided by a previous call's <code>NextToken</code> response to indicate where the output should continue from. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupingStatusesInput) -> dict:
    out: dict = {}
    out["Group"] = value["group"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filters" in value:
        import aws_sdk_resource_groups.types.list_grouping_statuses_filter_list

        out["Filters"] = (
            aws_sdk_resource_groups.types.list_grouping_statuses_filter_list.serialize_json(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGroupingStatusesInput:
    out: ListGroupingStatusesInput = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        out["group"] = data["Group"]
    else:
        raise DeserializationError("ListGroupingStatusesInput.group required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Filters" in data:
        import aws_sdk_resource_groups.types.list_grouping_statuses_filter_list

        out["filters"] = (
            aws_sdk_resource_groups.types.list_grouping_statuses_filter_list.deserialize_json(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
