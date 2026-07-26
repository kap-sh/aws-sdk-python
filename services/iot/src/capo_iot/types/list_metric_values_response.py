"""Generated from Smithy shape ``com.amazonaws.iot#ListMetricValuesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.metric_datum_list
    import capo_iot.types.next_token


class ListMetricValuesResponse(TypedDict, closed=True):
    metric_datum_list: NotRequired["capo_iot.types.metric_datum_list.MetricDatumList"]
    """<p>The data the thing reports for the metric during the specified time period.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>A token that can be used to retrieve the next set of results, or <code>null</code> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMetricValuesResponse) -> dict:
    out: dict = {}
    if "metric_datum_list" in value:
        import capo_iot.types.metric_datum_list

        out["metricDatumList"] = capo_iot.types.metric_datum_list.serialize_json(
            value["metric_datum_list"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMetricValuesResponse:
    out: ListMetricValuesResponse = {}  # type: ignore[typeddict-item]
    if "metricDatumList" in data:
        import capo_iot.types.metric_datum_list

        out["metric_datum_list"] = capo_iot.types.metric_datum_list.deserialize_json(
            data["metricDatumList"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
