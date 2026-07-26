"""Generated from Smithy shape ``com.amazonaws.iot#ListCustomMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.metric_names
    import capo_iot.types.next_token


class ListCustomMetricsResponse(TypedDict, closed=True):
    metric_names: NotRequired["capo_iot.types.metric_names.MetricNames"]
    """<p> The name of the custom metric. </p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p> A token that can be used to retrieve the next set of results, or <code>null</code> if there are no additional results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomMetricsResponse) -> dict:
    out: dict = {}
    if "metric_names" in value:
        import capo_iot.types.metric_names

        out["metricNames"] = capo_iot.types.metric_names.serialize_json(
            value["metric_names"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCustomMetricsResponse:
    out: ListCustomMetricsResponse = {}  # type: ignore[typeddict-item]
    if "metricNames" in data:
        import capo_iot.types.metric_names

        out["metric_names"] = capo_iot.types.metric_names.deserialize_json(
            data["metricNames"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
