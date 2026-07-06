"""Generated from Smithy shape ``com.amazonaws.opensearch#ListInsightsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.insight_entity
    import aws_sdk_opensearch.types.insight_page_size
    import aws_sdk_opensearch.types.insight_sort_order
    import aws_sdk_opensearch.types.insight_time_range
    import aws_sdk_opensearch.types.string


class ListInsightsRequest(TypedDict, closed=True):
    entity: "aws_sdk_opensearch.types.insight_entity.InsightEntity"
    """<p>The entity for which to list insights. Specifies the type and value of the entity, such as a domain name or Amazon Web Services account ID.</p>"""
    time_range: NotRequired[
        "aws_sdk_opensearch.types.insight_time_range.InsightTimeRange"
    ]
    """<p>The time range for filtering insights, specified as epoch millisecond timestamps.</p>"""
    sort_order: NotRequired[
        "aws_sdk_opensearch.types.insight_sort_order.InsightSortOrder"
    ]
    """<p>The sort order for the results. Possible values are <code>ASC</code> (ascending) and <code>DESC</code> (descending).</p>"""
    max_results: NotRequired[
        "aws_sdk_opensearch.types.insight_page_size.InsightPageSize"
    ]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>NextToken</code> to get the next page of results. Valid values are 1 to 500.</p>"""
    next_token: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>If your initial <code>ListInsights</code> operation returns a <code>NextToken</code>, include the returned <code>NextToken</code> in subsequent <code>ListInsights</code> operations to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInsightsRequest) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.insight_entity

    out["Entity"] = aws_sdk_opensearch.types.insight_entity.serialize_json(
        value["entity"]
    )
    if "time_range" in value:
        import aws_sdk_opensearch.types.insight_time_range

        out["TimeRange"] = aws_sdk_opensearch.types.insight_time_range.serialize_json(
            value["time_range"]
        )
    if "sort_order" in value:
        import aws_sdk_opensearch.types.insight_sort_order

        out["SortOrder"] = aws_sdk_opensearch.types.insight_sort_order.serialize_json(
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
        import aws_sdk_opensearch.types.insight_entity

        out["entity"] = aws_sdk_opensearch.types.insight_entity.deserialize_json(
            data["Entity"]
        )
    else:
        raise DeserializationError("ListInsightsRequest.entity required")
    if "TimeRange" in data:
        import aws_sdk_opensearch.types.insight_time_range

        out["time_range"] = (
            aws_sdk_opensearch.types.insight_time_range.deserialize_json(
                data["TimeRange"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_opensearch.types.insight_sort_order

        out["sort_order"] = (
            aws_sdk_opensearch.types.insight_sort_order.deserialize_json(
                data["SortOrder"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
