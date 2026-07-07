"""Generated from Smithy shape ``com.amazonaws.datazone#ListLineageNodeHistoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.edge_direction
    import aws_sdk_datazone.types.lineage_node_identifier
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.sort_order


class ListLineageNodeHistoryInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to list the history of the specified data lineage node.</p>"""
    max_results: NotRequired["aws_sdk_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of history items to return in a single call to ListLineageNodeHistory. When the number of memberships to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListLineageNodeHistory to list the next set of items.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of history items is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of items, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListLineageNodeHistory to list the next set of items.</p>"""
    identifier: "aws_sdk_datazone.types.lineage_node_identifier.LineageNodeIdentifier"
    """<p>The ID of the data lineage node whose history you want to list.</p>"""
    direction: NotRequired["aws_sdk_datazone.types.edge_direction.EdgeDirection"]
    """<p>The direction of the data lineage node refers to the lineage node having neighbors in that direction. For example, if direction is <code>UPSTREAM</code>, the <code>ListLineageNodeHistory</code> API responds with historical versions with upstream neighbors only.</p>"""
    event_timestamp_gte: NotRequired["datetime.datetime"]
    """<p>Specifies whether the action is to return data lineage node history from the time after the event timestamp.</p>"""
    event_timestamp_lte: NotRequired["datetime.datetime"]
    """<p>Specifies whether the action is to return data lineage node history from the time prior of the event timestamp.</p>"""
    sort_order: NotRequired["aws_sdk_datazone.types.sort_order.SortOrder"]
    """<p>The order by which you want data lineage node history to be sorted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLineageNodeHistoryInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListLineageNodeHistoryInput:
    out: ListLineageNodeHistoryInput = {}  # type: ignore[typeddict-item]
    return out
