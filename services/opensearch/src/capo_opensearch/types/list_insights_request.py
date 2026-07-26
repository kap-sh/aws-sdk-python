"""Generated from Smithy shape ``com.amazonaws.opensearch#ListInsightsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.insight_entity
    import capo_opensearch.types.insight_page_size
    import capo_opensearch.types.insight_sort_order
    import capo_opensearch.types.insight_time_range
    import capo_opensearch.types.string


class ListInsightsRequest(TypedDict, closed=True):
    entity: "capo_opensearch.types.insight_entity.InsightEntity"
    """<p>The entity for which to list insights. Specifies the type and value of the entity, such as a domain name or Amazon Web Services account ID.</p>"""
    time_range: NotRequired["capo_opensearch.types.insight_time_range.InsightTimeRange"]
    """<p>The time range for filtering insights, specified as epoch millisecond timestamps.</p>"""
    sort_order: NotRequired["capo_opensearch.types.insight_sort_order.InsightSortOrder"]
    """<p>The sort order for the results. Possible values are <code>ASC</code> (ascending) and <code>DESC</code> (descending).</p>"""
    max_results: NotRequired["capo_opensearch.types.insight_page_size.InsightPageSize"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>NextToken</code> to get the next page of results. Valid values are 1 to 500.</p>"""
    next_token: NotRequired["capo_opensearch.types.string.String"]
    """<p>If your initial <code>ListInsights</code> operation returns a <code>NextToken</code>, include the returned <code>NextToken</code> in subsequent <code>ListInsights</code> operations to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInsightsRequest) -> dict:
    out: dict = {}
    import capo_opensearch.types.insight_entity

    out["Entity"] = capo_opensearch.types.insight_entity.serialize_json(value["entity"])
    if "time_range" in value:
        import capo_opensearch.types.insight_time_range

        out["TimeRange"] = capo_opensearch.types.insight_time_range.serialize_json(
            value["time_range"]
        )
    if "sort_order" in value:
        import capo_opensearch.types.insight_sort_order

        out["SortOrder"] = capo_opensearch.types.insight_sort_order.serialize_json(
            value["sort_order"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInsightsRequest:
    out: ListInsightsRequest = {}  # type: ignore[typeddict-item]
    if "Entity" in data:
        import capo_opensearch.types.insight_entity

        out["entity"] = capo_opensearch.types.insight_entity.deserialize_json(
            data["Entity"]
        )
    else:
        raise DeserializationError("ListInsightsRequest.entity required")
    if "TimeRange" in data:
        import capo_opensearch.types.insight_time_range

        out["time_range"] = capo_opensearch.types.insight_time_range.deserialize_json(
            data["TimeRange"]
        )
    if "SortOrder" in data:
        import capo_opensearch.types.insight_sort_order

        out["sort_order"] = capo_opensearch.types.insight_sort_order.deserialize_json(
            data["SortOrder"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
