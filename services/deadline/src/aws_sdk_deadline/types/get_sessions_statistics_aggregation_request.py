"""Generated from Smithy shape ``com.amazonaws.deadline#GetSessionsStatisticsAggregationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.aggregation_id
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.max_results
    import aws_sdk_deadline.types.next_token


class GetSessionsStatisticsAggregationRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The identifier of the farm to include in the statistics. This should be the same as the farm ID used in the call to the <code>StartSessionsStatisticsAggregation</code> operation.</p>"""
    next_token: NotRequired["aws_sdk_deadline.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>"""
    max_results: "aws_sdk_deadline.types.max_results.MaxResults"
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    aggregation_id: "aws_sdk_deadline.types.aggregation_id.AggregationId"
    """<p>The identifier returned by the <code>StartSessionsStatisticsAggregation</code> operation that identifies the aggregated statistics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionsStatisticsAggregationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSessionsStatisticsAggregationRequest:
    out: GetSessionsStatisticsAggregationRequest = {}  # type: ignore[typeddict-item]
    return out
