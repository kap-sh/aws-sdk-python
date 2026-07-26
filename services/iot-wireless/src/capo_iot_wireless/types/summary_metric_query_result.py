"""Generated from Smithy shape ``com.amazonaws.iotwireless#SummaryMetricQueryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.aggregation_period
    import capo_iot_wireless.types.dimensions
    import capo_iot_wireless.types.metric_name
    import capo_iot_wireless.types.metric_query_end_timestamp
    import capo_iot_wireless.types.metric_query_error
    import capo_iot_wireless.types.metric_query_id
    import capo_iot_wireless.types.metric_query_start_timestamp
    import capo_iot_wireless.types.metric_query_status
    import capo_iot_wireless.types.metric_query_timestamps
    import capo_iot_wireless.types.metric_query_values
    import capo_iot_wireless.types.metric_unit


class SummaryMetricQueryResult(TypedDict, closed=True):
    query_id: NotRequired["capo_iot_wireless.types.metric_query_id.MetricQueryId"]
    """<p>The ID of the summary metric results query operation.</p>"""
    query_status: NotRequired[
        "capo_iot_wireless.types.metric_query_status.MetricQueryStatus"
    ]
    """<p>The status of the summary metric query result.</p>"""
    error: NotRequired["capo_iot_wireless.types.metric_query_error.MetricQueryError"]
    """<p>The error message for the summary metric query result.</p>"""
    metric_name: NotRequired["capo_iot_wireless.types.metric_name.MetricName"]
    """<p>The name of the summary metric query result.</p>"""
    dimensions: NotRequired["capo_iot_wireless.types.dimensions.Dimensions"]
    """<p>The dimensions of the metric.</p>"""
    aggregation_period: NotRequired[
        "capo_iot_wireless.types.aggregation_period.AggregationPeriod"
    ]
    """<p>The aggregation period of the metric.</p>"""
    start_timestamp: NotRequired[
        "capo_iot_wireless.types.metric_query_start_timestamp.MetricQueryStartTimestamp"
    ]
    """<p>The start timestamp for the summary metric query.</p>"""
    end_timestamp: NotRequired[
        "capo_iot_wireless.types.metric_query_end_timestamp.MetricQueryEndTimestamp"
    ]
    """<p>The end timestamp for the summary metric query.</p>"""
    timestamps: NotRequired[
        "capo_iot_wireless.types.metric_query_timestamps.MetricQueryTimestamps"
    ]
    """<p>The timestamp of each aggregation result.</p>"""
    values: NotRequired["capo_iot_wireless.types.metric_query_values.MetricQueryValues"]
    """<p>The list of aggregated summary metric query results.</p>"""
    unit: NotRequired["capo_iot_wireless.types.metric_unit.MetricUnit"]
    """<p>The units of measurement to be used for interpreting the aggregation result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SummaryMetricQueryResult) -> dict:
    out: dict = {}
    if "query_id" in value:
        out["QueryId"] = value["query_id"]
    if "query_status" in value:
        import capo_iot_wireless.types.metric_query_status

        out["QueryStatus"] = capo_iot_wireless.types.metric_query_status.serialize_json(
            value["query_status"]
        )
    if "error" in value:
        out["Error"] = value["error"]
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
    if "timestamps" in value:
        import capo_iot_wireless.types.metric_query_timestamps

        out["Timestamps"] = (
            capo_iot_wireless.types.metric_query_timestamps.serialize_json(
                value["timestamps"]
            )
        )
    if "values" in value:
        import capo_iot_wireless.types.metric_query_values

        out["Values"] = capo_iot_wireless.types.metric_query_values.serialize_json(
            value["values"]
        )
    if "unit" in value:
        out["Unit"] = value["unit"]
    return out


def deserialize_json(data: dict) -> SummaryMetricQueryResult:
    out: SummaryMetricQueryResult = {}  # type: ignore[typeddict-item]
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    if "QueryStatus" in data:
        import capo_iot_wireless.types.metric_query_status

        out["query_status"] = (
            capo_iot_wireless.types.metric_query_status.deserialize_json(
                data["QueryStatus"]
            )
        )
    if "Error" in data:
        out["error"] = data["Error"]
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
    if "Timestamps" in data:
        import capo_iot_wireless.types.metric_query_timestamps

        out["timestamps"] = (
            capo_iot_wireless.types.metric_query_timestamps.deserialize_json(
                data["Timestamps"]
            )
        )
    if "Values" in data:
        import capo_iot_wireless.types.metric_query_values

        out["values"] = capo_iot_wireless.types.metric_query_values.deserialize_json(
            data["Values"]
        )
    if "Unit" in data:
        out["unit"] = data["Unit"]
    return out
