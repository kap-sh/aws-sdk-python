"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListMonitoredResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.list_monitored_resources_filters
    import capo_devops_guru.types.list_monitored_resources_max_results
    import capo_devops_guru.types.uuid_next_token


class ListMonitoredResourcesRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_devops_guru.types.list_monitored_resources_filters.ListMonitoredResourcesFilters"
    ]
    """<p> Filters to determine which monitored resources you want to retrieve. You can filter by resource type or resource permission status. </p>"""
    max_results: NotRequired[
        "capo_devops_guru.types.list_monitored_resources_max_results.ListMonitoredResourcesMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["capo_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMonitoredResourcesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_devops_guru.types.list_monitored_resources_filters

        out["Filters"] = (
            capo_devops_guru.types.list_monitored_resources_filters.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMonitoredResourcesRequest:
    out: ListMonitoredResourcesRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import capo_devops_guru.types.list_monitored_resources_filters

        out["filters"] = (
            capo_devops_guru.types.list_monitored_resources_filters.deserialize_json(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
