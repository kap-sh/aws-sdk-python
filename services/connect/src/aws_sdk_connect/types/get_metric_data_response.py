"""Generated from Smithy shape ``com.amazonaws.connect#GetMetricDataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.historical_metric_results
    import aws_sdk_connect.types.next_token


class GetMetricDataResponse(TypedDict):
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p> <p>The token expires after 5 minutes from the time it is created. Subsequent requests that use the token must use the same request parameters as the request that generated the token.</p>"""
    metric_results: NotRequired[
        "aws_sdk_connect.types.historical_metric_results.HistoricalMetricResults"
    ]
    """<p>Information about the historical metrics.</p> <p>If no grouping is specified, a summary of metric data is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMetricDataResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "metric_results" in value:
        import aws_sdk_connect.types.historical_metric_results

        out["MetricResults"] = (
            aws_sdk_connect.types.historical_metric_results.serialize_json(
                value["metric_results"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMetricDataResponse:
    out: GetMetricDataResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MetricResults" in data:
        import aws_sdk_connect.types.historical_metric_results

        out["metric_results"] = (
            aws_sdk_connect.types.historical_metric_results.deserialize_json(
                data["MetricResults"]
            )
        )
    return out
