"""Generated from Smithy shape ``com.amazonaws.iotwireless#SummaryMetricQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.aggregation_period
    import capo_iot_wireless.types.dimensions
    import capo_iot_wireless.types.metric_name
    import capo_iot_wireless.types.metric_query_end_timestamp
    import capo_iot_wireless.types.metric_query_id
    import capo_iot_wireless.types.metric_query_start_timestamp


class SummaryMetricQuery(TypedDict, closed=True):
    query_id: NotRequired["capo_iot_wireless.types.metric_query_id.MetricQueryId"]
    """<p>The id of the summary metric query.</p>"""
    metric_name: NotRequired["capo_iot_wireless.types.metric_name.MetricName"]
    """<p>The name of the metric.</p>"""
    dimensions: NotRequired["capo_iot_wireless.types.dimensions.Dimensions"]
    """<p>The dimensions of the summary metric.</p>"""
    aggregation_period: NotRequired[
        "capo_iot_wireless.types.aggregation_period.AggregationPeriod"
    ]
    """<p>The aggregation period of the summary metric.</p>"""
    start_timestamp: NotRequired[
        "capo_iot_wireless.types.metric_query_start_timestamp.MetricQueryStartTimestamp"
    ]
    """<p>The start timestamp for the summary metric query.</p>"""
    end_timestamp: NotRequired[
        "capo_iot_wireless.types.metric_query_end_timestamp.MetricQueryEndTimestamp"
    ]
    """<p>The end timestamp for the summary metric query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SummaryMetricQuery) -> dict:
    out: dict = {}
    if "query_id" in value:
        out["QueryId"] = value["query_id"]
    if "metric_name" in value:
        import capo_iot_wireless.types.metric_name

        out["MetricName"] = capo_iot_wireless.types.metric_name.serialize_json(
            value["metric_name"]
        )
    if "dimensions" in value:
        import capo_iot_wireless.types.dimensions

        out["Dimensions"] = capo_iot_wireless.types.dimensions.serialize_json(
            value["dimensions"]
        )
    if "aggregation_period" in value:
        import capo_iot_wireless.types.aggregation_period

        out["AggregationPeriod"] = (
            capo_iot_wireless.types.aggregation_period.serialize_json(
                value["aggregation_period"]
            )
        )
    if "start_timestamp" in value:
        import capo_iot_wireless.types.metric_query_start_timestamp

        out["StartTimestamp"] = (
            capo_iot_wireless.types.metric_query_start_timestamp.serialize_json(
                value["start_timestamp"]
            )
        )
    if "end_timestamp" in value:
        import capo_iot_wireless.types.metric_query_end_timestamp

        out["EndTimestamp"] = (
            capo_iot_wireless.types.metric_query_end_timestamp.serialize_json(
                value["end_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> SummaryMetricQuery:
    out: SummaryMetricQuery = {}  # type: ignore[typeddict-item]
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    if "MetricName" in data:
        import capo_iot_wireless.types.metric_name

        out["metric_name"] = capo_iot_wireless.types.metric_name.deserialize_json(
            data["MetricName"]
        )
    if "Dimensions" in data:
        import capo_iot_wireless.types.dimensions

        out["dimensions"] = capo_iot_wireless.types.dimensions.deserialize_json(
            data["Dimensions"]
        )
    if "AggregationPeriod" in data:
        import capo_iot_wireless.types.aggregation_period

        out["aggregation_period"] = (
            capo_iot_wireless.types.aggregation_period.deserialize_json(
                data["AggregationPeriod"]
            )
        )
    if "StartTimestamp" in data:
        import capo_iot_wireless.types.metric_query_start_timestamp

        out["start_timestamp"] = (
            capo_iot_wireless.types.metric_query_start_timestamp.deserialize_json(
                data["StartTimestamp"]
            )
        )
    if "EndTimestamp" in data:
        import capo_iot_wireless.types.metric_query_end_timestamp

        out["end_timestamp"] = (
            capo_iot_wireless.types.metric_query_end_timestamp.deserialize_json(
                data["EndTimestamp"]
            )
        )
    return out
