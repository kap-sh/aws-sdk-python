"""Generated from Smithy shape ``com.amazonaws.batch#ListConsumableResourcesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.list_consumable_resources_filter_list
    import aws_sdk_batch.types.string


class ListConsumableResourcesRequest(TypedDict):
    filters: NotRequired[
        "aws_sdk_batch.types.list_consumable_resources_filter_list.ListConsumableResourcesFilterList"
    ]
    """<p>The filters to apply to the consumable resource list query. If used, only those consumable resources that match the filter are listed. Filter names and values can be:</p> <ul> <li> <p>name: <code>CONSUMABLE_RESOURCE_NAME </code> </p> <p>values: case-insensitive matches for the consumable resource name. If a filter value ends with an asterisk (*), it matches any consumable resource name that begins with the string before the '*'.</p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The maximum number of results returned by <code>ListConsumableResources</code> in paginated output. When this parameter is used, <code>ListConsumableResources</code> only returns <code>maxResults</code> results in a single page and a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListConsumableResources</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListConsumableResources</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>"""
    next_token: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>ListConsumableResources</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConsumableResourcesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_batch.types.list_consumable_resources_filter_list

        out["filters"] = (
            aws_sdk_batch.types.list_consumable_resources_filter_list.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConsumableResourcesRequest:
    out: ListConsumableResourcesRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_batch.types.list_consumable_resources_filter_list

        out["filters"] = (
            aws_sdk_batch.types.list_consumable_resources_filter_list.deserialize_json(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
