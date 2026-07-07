"""Generated from Smithy shape ``com.amazonaws.connect#GetMetricDataV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.metric_results_v2
    import aws_sdk_connect.types.next_token2500


class GetMetricDataV2Response(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_connect.types.next_token2500.NextToken2500"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    metric_results: NotRequired[
        "aws_sdk_connect.types.metric_results_v2.MetricResultsV2"
    ]
    """<p>Information about the metrics requested in the API request If no grouping is specified, a summary of metric data is returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMetricDataV2Response) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "metric_results" in value:
        import aws_sdk_connect.types.metric_results_v2

        out["MetricResults"] = aws_sdk_connect.types.metric_results_v2.serialize_json(
            value["metric_results"]
        )
    return out


def deserialize_json(data: dict) -> GetMetricDataV2Response:
    out: GetMetricDataV2Response = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MetricResults" in data:
        import aws_sdk_connect.types.metric_results_v2

        out["metric_results"] = (
            aws_sdk_connect.types.metric_results_v2.deserialize_json(
                data["MetricResults"]
            )
        )
    return out
