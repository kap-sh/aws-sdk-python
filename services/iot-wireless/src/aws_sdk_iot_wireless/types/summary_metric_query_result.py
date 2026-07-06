"""Generated from Smithy shape ``com.amazonaws.iotwireless#SummaryMetricQueryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.aggregation_period
    import aws_sdk_iot_wireless.types.dimensions
    import aws_sdk_iot_wireless.types.metric_name
    import aws_sdk_iot_wireless.types.metric_query_end_timestamp
    import aws_sdk_iot_wireless.types.metric_query_error
    import aws_sdk_iot_wireless.types.metric_query_id
    import aws_sdk_iot_wireless.types.metric_query_start_timestamp
    import aws_sdk_iot_wireless.types.metric_query_status
    import aws_sdk_iot_wireless.types.metric_query_timestamps
    import aws_sdk_iot_wireless.types.metric_query_values
    import aws_sdk_iot_wireless.types.metric_unit


class SummaryMetricQueryResult(TypedDict, closed=True):
    query_id: NotRequired["aws_sdk_iot_wireless.types.metric_query_id.MetricQueryId"]
    """<p>The ID of the summary metric results query operation.</p>"""
    query_status: NotRequired[
        "aws_sdk_iot_wireless.types.metric_query_status.MetricQueryStatus"
    ]
    """<p>The status of the summary metric query result.</p>"""
    error: NotRequired["aws_sdk_iot_wireless.types.metric_query_error.MetricQueryError"]
    """<p>The error message for the summary metric query result.</p>"""
    metric_name: NotRequired["aws_sdk_iot_wireless.types.metric_name.MetricName"]
    """<p>The name of the summary metric query result.</p>"""
    dimensions: NotRequired["aws_sdk_iot_wireless.types.dimensions.Dimensions"]
    """<p>The dimensions of the metric.</p>"""
    aggregation_period: NotRequired[
        "aws_sdk_iot_wireless.types.aggregation_period.AggregationPeriod"
    ]
    """<p>The aggregation period of the metric.</p>"""
    start_timestamp: NotRequired[
        "aws_sdk_iot_wireless.types.metric_query_start_timestamp.MetricQueryStartTimestamp"
    ]
    """<p>The start timestamp for the summary metric query.</p>"""
    end_timestamp: NotRequired[
        "aws_sdk_iot_wireless.types.metric_query_end_timestamp.MetricQueryEndTimestamp"
    ]
    """<p>The end timestamp for the summary metric query.</p>"""
    timestamps: NotRequired[
        "aws_sdk_iot_wireless.types.metric_query_timestamps.MetricQueryTimestamps"
    ]
    """<p>The timestamp of each aggregation result.</p>"""
    values: NotRequired[
        "aws_sdk_iot_wireless.types.metric_query_values.MetricQueryValues"
    ]
    """<p>The list of aggregated summary metric query results.</p>"""
    unit: NotRequired["aws_sdk_iot_wireless.types.metric_unit.MetricUnit"]
    """<p>The units of measurement to be used for interpreting the aggregation result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SummaryMetricQueryResult) -> dict:
    out: dict = {}
    if "query_id" in value:
        out["QueryId"] = value["query_id"]
    if "query_status" in value:
        import aws_sdk_iot_wireless.types.metric_query_status

        out["QueryStatus"] = (
            aws_sdk_iot_wireless.types.metric_query_status.serialize_json(
                value["query_status"]
            )
        )
    if "error" in value:
        out["Error"] = value["error"]
    if "metric_name" in value:
        import aws_sdk_iot_wireless.types.metric_name

        out["MetricName"] = aws_sdk_iot_wireless.types.metric_name.serialize_json(
            value["metric_name"]
        )
    if "dimensions" in value:
        import aws_sdk_iot_wireless.types.dimensions

        out["Dimensions"] = aws_sdk_iot_wireless.types.dimensions.serialize_json(
            value["dimensions"]
        )
    if "aggregation_period" in value:
        import aws_sdk_iot_wireless.types.aggregation_period

        out["AggregationPeriod"] = (
            aws_sdk_iot_wireless.types.aggregation_period.serialize_json(
                value["aggregation_period"]
            )
        )
    if "start_timestamp" in value:
        import aws_sdk_iot_wireless.types.metric_query_start_timestamp

        out["StartTimestamp"] = (
            aws_sdk_iot_wireless.types.metric_query_start_timestamp.serialize_json(
                value["start_timestamp"]
            )
        )
    if "end_timestamp" in value:
        import aws_sdk_iot_wireless.types.metric_query_end_timestamp

        out["EndTimestamp"] = (
            aws_sdk_iot_wireless.types.metric_query_end_timestamp.serialize_json(
                value["end_timestamp"]
            )
        )
    if "timestamps" in value:
        import aws_sdk_iot_wireless.types.metric_query_timestamps

        out["Timestamps"] = (
            aws_sdk_iot_wireless.types.metric_query_timestamps.serialize_json(
                value["timestamps"]
            )
        )
    if "values" in value:
        import aws_sdk_iot_wireless.types.metric_query_values

        out["Values"] = aws_sdk_iot_wireless.types.metric_query_values.serialize_json(
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
        import aws_sdk_iot_wireless.types.metric_query_status

        out["query_status"] = (
            aws_sdk_iot_wireless.types.metric_query_status.deserialize_json(
                data["QueryStatus"]
            )
        )
    if "Error" in data:
        out["error"] = data["Error"]
    if "MetricName" in data:
        import aws_sdk_iot_wireless.types.metric_name

        out["metric_name"] = aws_sdk_iot_wireless.types.metric_name.deserialize_json(
            data["MetricName"]
        )
    if "Dimensions" in data:
        import aws_sdk_iot_wireless.types.dimensions

        out["dimensions"] = aws_sdk_iot_wireless.types.dimensions.deserialize_json(
            data["Dimensions"]
        )
    if "AggregationPeriod" in data:
        import aws_sdk_iot_wireless.types.aggregation_period

        out["aggregation_period"] = (
            aws_sdk_iot_wireless.types.aggregation_period.deserialize_json(
                data["AggregationPeriod"]
            )
        )
    if "StartTimestamp" in data:
        import aws_sdk_iot_wireless.types.metric_query_start_timestamp

        out["start_timestamp"] = (
            aws_sdk_iot_wireless.types.metric_query_start_timestamp.deserialize_json(
                data["StartTimestamp"]
            )
        )
    if "EndTimestamp" in data:
        import aws_sdk_iot_wireless.types.metric_query_end_timestamp

        out["end_timestamp"] = (
            aws_sdk_iot_wireless.types.metric_query_end_timestamp.deserialize_json(
                data["EndTimestamp"]
            )
        )
    if "Timestamps" in data:
        import aws_sdk_iot_wireless.types.metric_query_timestamps

        out["timestamps"] = (
            aws_sdk_iot_wireless.types.metric_query_timestamps.deserialize_json(
                data["Timestamps"]
            )
        )
    if "Values" in data:
        import aws_sdk_iot_wireless.types.metric_query_values

        out["values"] = aws_sdk_iot_wireless.types.metric_query_values.deserialize_json(
            data["Values"]
        )
    if "Unit" in data:
        out["unit"] = data["Unit"]
    return out
