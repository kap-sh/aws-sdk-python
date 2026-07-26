"""Generated from Smithy shape ``com.amazonaws.configservice#GetAggregateDiscoveredResourceCountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.grouped_resource_count_list
    import capo_config_service.types.long
    import capo_config_service.types.next_token
    import capo_config_service.types.string_with_char_limit256


class GetAggregateDiscoveredResourceCountsResponse(TypedDict, closed=True):
    total_discovered_resources: "capo_config_service.types.long.Long"
    """<p>The total number of resources that are present in an aggregator with the filters that you provide.</p>"""
    group_by_key: NotRequired[
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>The key passed into the request object. If <code>GroupByKey</code> is not provided, the result will be empty.</p>"""
    grouped_resource_counts: NotRequired[
        "capo_config_service.types.grouped_resource_count_list.GroupedResourceCountList"
    ]
    """<p>Returns a list of GroupedResourceCount objects.</p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAggregateDiscoveredResourceCountsResponse) -> dict:
    out: dict = {}
    out["TotalDiscoveredResources"] = value.get("total_discovered_resources", 0)
    if "group_by_key" in value:
        out["GroupByKey"] = value["group_by_key"]
    if "grouped_resource_counts" in value:
        import capo_config_service.types.grouped_resource_count_list

        out["GroupedResourceCounts"] = (
            capo_config_service.types.grouped_resource_count_list.serialize_aws_json_1_1(
                value["grouped_resource_counts"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetAggregateDiscoveredResourceCountsResponse:
    out: GetAggregateDiscoveredResourceCountsResponse = {}  # type: ignore[typeddict-item]
    if "TotalDiscoveredResources" in data:
        out["total_discovered_resources"] = data["TotalDiscoveredResources"]
    else:
        out["total_discovered_resources"] = 0
    if "GroupByKey" in data:
        out["group_by_key"] = data["GroupByKey"]
    if "GroupedResourceCounts" in data:
        import capo_config_service.types.grouped_resource_count_list

        out["grouped_resource_counts"] = (
            capo_config_service.types.grouped_resource_count_list.deserialize_aws_json_1_1(
                data["GroupedResourceCounts"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
