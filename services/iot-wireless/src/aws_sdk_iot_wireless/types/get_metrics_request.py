"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetMetricsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.summary_metric_queries


class GetMetricsRequest(TypedDict):
    summary_metric_queries: NotRequired[
        "aws_sdk_iot_wireless.types.summary_metric_queries.SummaryMetricQueries"
    ]
    """<p>The list of queries to retrieve the summary metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMetricsRequest) -> dict:
    out: dict = {}
    if "summary_metric_queries" in value:
        import aws_sdk_iot_wireless.types.summary_metric_queries

        out["SummaryMetricQueries"] = (
            aws_sdk_iot_wireless.types.summary_metric_queries.serialize_json(
                value["summary_metric_queries"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMetricsRequest:
    out: GetMetricsRequest = {}  # type: ignore[typeddict-item]
    if "SummaryMetricQueries" in data:
        import aws_sdk_iot_wireless.types.summary_metric_queries

        out["summary_metric_queries"] = (
            aws_sdk_iot_wireless.types.summary_metric_queries.deserialize_json(
                data["SummaryMetricQueries"]
            )
        )
    return out
