"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetMetricsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.summary_metric_query_results


class GetMetricsResponse(TypedDict):
    summary_metric_query_results: NotRequired[
        "aws_sdk_iot_wireless.types.summary_metric_query_results.SummaryMetricQueryResults"
    ]
    """<p>The list of summary metrics that were retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMetricsResponse) -> dict:
    out: dict = {}
    if "summary_metric_query_results" in value:
        import aws_sdk_iot_wireless.types.summary_metric_query_results

        out["SummaryMetricQueryResults"] = (
            aws_sdk_iot_wireless.types.summary_metric_query_results.serialize_json(
                value["summary_metric_query_results"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMetricsResponse:
    out: GetMetricsResponse = {}  # type: ignore[typeddict-item]
    if "SummaryMetricQueryResults" in data:
        import aws_sdk_iot_wireless.types.summary_metric_query_results

        out["summary_metric_query_results"] = (
            aws_sdk_iot_wireless.types.summary_metric_query_results.deserialize_json(
                data["SummaryMetricQueryResults"]
            )
        )
    return out
