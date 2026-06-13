"""Generated from Smithy shape ``com.amazonaws.datazone#SearchListingsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.aggregation_output_list
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.search_result_items


class SearchListingsOutput(TypedDict):
    items: NotRequired["aws_sdk_datazone.types.search_result_items.SearchResultItems"]
    """<p>The results of the <code>SearchListings</code> action.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of results is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of results, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>SearchListings</code> to list the next set of results.</p>"""
    total_match_count: NotRequired["int"]
    """<p>Total number of search results.</p>"""
    aggregates: NotRequired[
        "aws_sdk_datazone.types.aggregation_output_list.AggregationOutputList"
    ]
    """<p>Contains computed counts grouped by field values based on the requested aggregation attributes for the matching listings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchListingsOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_datazone.types.search_result_items

        out["items"] = aws_sdk_datazone.types.search_result_items.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "total_match_count" in value:
        out["totalMatchCount"] = value["total_match_count"]
    if "aggregates" in value:
        import aws_sdk_datazone.types.aggregation_output_list

        out["aggregates"] = (
            aws_sdk_datazone.types.aggregation_output_list.serialize_json(
                value["aggregates"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchListingsOutput:
    out: SearchListingsOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_datazone.types.search_result_items

        out["items"] = aws_sdk_datazone.types.search_result_items.deserialize_json(
            data["items"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "totalMatchCount" in data:
        out["total_match_count"] = data["totalMatchCount"]
    if "aggregates" in data:
        import aws_sdk_datazone.types.aggregation_output_list

        out["aggregates"] = (
            aws_sdk_datazone.types.aggregation_output_list.deserialize_json(
                data["aggregates"]
            )
        )
    return out
