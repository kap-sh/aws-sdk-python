"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetMetricsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.summary_metric_queries


class GetMetricsRequest(TypedDict, closed=True):
    summary_metric_queries: NotRequired[
        "capo_iot_wireless.types.summary_metric_queries.SummaryMetricQueries"
    ]
    """<p>The list of queries to retrieve the summary metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMetricsRequest) -> dict:
    out: dict = {}
    if "summary_metric_queries" in value:
        import capo_iot_wireless.types.summary_metric_queries

        out["SummaryMetricQueries"] = (
            capo_iot_wireless.types.summary_metric_queries.serialize_json(
                value["summary_metric_queries"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMetricsRequest:
    out: GetMetricsRequest = {}  # type: ignore[typeddict-item]
    if "SummaryMetricQueries" in data:
        import capo_iot_wireless.types.summary_metric_queries

        out["summary_metric_queries"] = (
            capo_iot_wireless.types.summary_metric_queries.deserialize_json(
                data["SummaryMetricQueries"]
            )
        )
    return out
