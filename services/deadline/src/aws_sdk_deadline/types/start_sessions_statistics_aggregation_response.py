"""Generated from Smithy shape ``com.amazonaws.deadline#StartSessionsStatisticsAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.aggregation_id


class StartSessionsStatisticsAggregationResponse(TypedDict, closed=True):
    aggregation_id: "aws_sdk_deadline.types.aggregation_id.AggregationId"
    """<p>A unique identifier for the aggregated statistics. Use this identifier with the <code>GetAggregatedStatisticsForSessions</code> operation to return the statistics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSessionsStatisticsAggregationResponse) -> dict:
    out: dict = {}
    out["aggregationId"] = value["aggregation_id"]
    return out


def deserialize_json(data: dict) -> StartSessionsStatisticsAggregationResponse:
    out: StartSessionsStatisticsAggregationResponse = {}  # type: ignore[typeddict-item]
    if "aggregationId" in data:
        out["aggregation_id"] = data["aggregationId"]
    else:
        raise DeserializationError(
            "StartSessionsStatisticsAggregationResponse.aggregation_id required"
        )
    return out
