"""Generated from Smithy shape ``com.amazonaws.connect#GetCurrentMetricDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.approximate_total_count
    import aws_sdk_connect.types.current_metric_results
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.timestamp


class GetCurrentMetricDataResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p> <p>The token expires after 5 minutes from the time it is created. Subsequent requests that use the token must use the same request parameters as the request that generated the token.</p>"""
    metric_results: NotRequired[
        "aws_sdk_connect.types.current_metric_results.CurrentMetricResults"
    ]
    """<p>Information about the real-time metrics.</p>"""
    data_snapshot_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The time at which the metrics were retrieved and cached for pagination.</p>"""
    approximate_total_count: NotRequired[
        "aws_sdk_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The total count of the result, regardless of the current page size. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCurrentMetricDataResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "metric_results" in value:
        import aws_sdk_connect.types.current_metric_results

        out["MetricResults"] = (
            aws_sdk_connect.types.current_metric_results.serialize_json(
                value["metric_results"]
            )
        )
    if "data_snapshot_time" in value:
        import aws_sdk_connect.types.timestamp

        out["DataSnapshotTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["data_snapshot_time"]
        )
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> GetCurrentMetricDataResponse:
    out: GetCurrentMetricDataResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MetricResults" in data:
        import aws_sdk_connect.types.current_metric_results

        out["metric_results"] = (
            aws_sdk_connect.types.current_metric_results.deserialize_json(
                data["MetricResults"]
            )
        )
    if "DataSnapshotTime" in data:
        import aws_sdk_connect.types.timestamp

        out["data_snapshot_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["DataSnapshotTime"]
        )
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
