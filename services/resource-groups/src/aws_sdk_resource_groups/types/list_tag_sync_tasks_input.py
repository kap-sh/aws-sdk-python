"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ListTagSyncTasksInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.list_tag_sync_tasks_filter_list
    import aws_sdk_resource_groups.types.max_results
    import aws_sdk_resource_groups.types.next_token


class ListTagSyncTasksInput(TypedDict, closed=True):
    filters: NotRequired[
        "aws_sdk_resource_groups.types.list_tag_sync_tasks_filter_list.ListTagSyncTasksFilterList"
    ]
    """<p>The Amazon resource name (ARN) or name of the application group for which you want to return a list of tag-sync tasks. </p>"""
    max_results: NotRequired["aws_sdk_resource_groups.types.max_results.MaxResults"]
    """<p>The maximum number of results to be included in the response. </p>"""
    next_token: NotRequired["aws_sdk_resource_groups.types.next_token.NextToken"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value provided by a previous call's <code>NextToken</code> response to indicate where the output should continue from. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagSyncTasksInput) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_resource_groups.types.list_tag_sync_tasks_filter_list

        out["Filters"] = (
            aws_sdk_resource_groups.types.list_tag_sync_tasks_filter_list.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTagSyncTasksInput:
    out: ListTagSyncTasksInput = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_resource_groups.types.list_tag_sync_tasks_filter_list

        out["filters"] = (
            aws_sdk_resource_groups.types.list_tag_sync_tasks_filter_list.deserialize_json(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
