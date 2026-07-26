"""Generated from Smithy shape ``com.amazonaws.lightsail#GetBucketMetricDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.bucket_metric_name
    import capo_lightsail.types.bucket_name
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.metric_period
    import capo_lightsail.types.metric_statistic_list
    import capo_lightsail.types.metric_unit


class GetBucketMetricDataRequest(TypedDict, closed=True):
    bucket_name: "capo_lightsail.types.bucket_name.BucketName"
    """<p>The name of the bucket for which to get metric data.</p>"""
    metric_name: "capo_lightsail.types.bucket_metric_name.BucketMetricName"
    """<p>The metric for which you want to return information.</p> <p>Valid bucket metric names are listed below, along with the most useful statistics to include in your request, and the published unit value.</p> <note> <p>These bucket metrics are reported once per day.</p> </note> <ul> <li> <p> <b> <code>BucketSizeBytes</code> </b> - The amount of data in bytes stored in a bucket. This value is calculated by summing the size of all objects in the bucket (including object versions), including the size of all parts for all incomplete multipart uploads to the bucket.</p> <p>Statistics: The most useful statistic is <code>Maximum</code>.</p> <p>Unit: The published unit is <code>Bytes</code>.</p> </li> <li> <p> <b> <code>NumberOfObjects</code> </b> - The total number of objects stored in a bucket. This value is calculated by counting all objects in the bucket (including object versions) and the total number of parts for all incomplete multipart uploads to the bucket.</p> <p>Statistics: The most useful statistic is <code>Average</code>.</p> <p>Unit: The published unit is <code>Count</code>.</p> </li> </ul>"""
    start_time: "capo_lightsail.types.iso_date.IsoDate"
    """<p>The timestamp indicating the earliest data to be returned.</p>"""
    end_time: "capo_lightsail.types.iso_date.IsoDate"
    """<p>The timestamp indicating the latest data to be returned.</p>"""
    period: "capo_lightsail.types.metric_period.MetricPeriod"
    """<p>The granularity, in seconds, of the returned data points.</p> <note> <p>Bucket storage metrics are reported once per day. Therefore, you should specify a period of 86400 seconds, which is the number of seconds in a day.</p> </note>"""
    statistics: "capo_lightsail.types.metric_statistic_list.MetricStatisticList"
    """<p>The statistic for the metric.</p> <p>The following statistics are available:</p> <ul> <li> <p> <code>Minimum</code> - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.</p> </li> <li> <p> <code>Maximum</code> - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.</p> </li> <li> <p> <code>Sum</code> - The sum of all values submitted for the matching metric. You can use this statistic to determine the total volume of a metric.</p> </li> <li> <p> <code>Average</code> - The value of <code>Sum</code> / <code>SampleCount</code> during the specified period. By comparing this statistic with the <code>Minimum</code> and <code>Maximum</code> values, you can determine the full scope of a metric and how close the average use is to the <code>Minimum</code> and <code>Maximum</code> values. This comparison helps you to know when to increase or decrease your resources.</p> </li> <li> <p> <code>SampleCount</code> - The count, or number, of data points used for the statistical calculation.</p> </li> </ul>"""
    unit: "capo_lightsail.types.metric_unit.MetricUnit"
    """<p>The unit for the metric data request.</p> <p>Valid units depend on the metric data being requested. For the valid units with each available metric, see the <code>metricName</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBucketMetricDataRequest) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    import capo_lightsail.types.bucket_metric_name

    out["metricName"] = capo_lightsail.types.bucket_metric_name.serialize_aws_json_1_1(
        value["metric_name"]
    )
    import capo_lightsail.types.iso_date

    out["startTime"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
        value["start_time"]
    )
    import capo_lightsail.types.iso_date

    out["endTime"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
        value["end_time"]
    )
    out["period"] = value["period"]
    import capo_lightsail.types.metric_statistic_list

    out["statistics"] = (
        capo_lightsail.types.metric_statistic_list.serialize_aws_json_1_1(
            value["statistics"]
        )
    )
    import capo_lightsail.types.metric_unit

    out["unit"] = capo_lightsail.types.metric_unit.serialize_aws_json_1_1(value["unit"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBucketMetricDataRequest:
    out: GetBucketMetricDataRequest = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("GetBucketMetricDataRequest.bucket_name required")
    if "metricName" in data:
        import capo_lightsail.types.bucket_metric_name

        out["metric_name"] = (
            capo_lightsail.types.bucket_metric_name.deserialize_aws_json_1_1(
                data["metricName"]
            )
        )
    else:
        raise DeserializationError("GetBucketMetricDataRequest.metric_name required")
    if "startTime" in data:
        import capo_lightsail.types.iso_date

        out["start_time"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["startTime"]
        )
    else:
        raise DeserializationError("GetBucketMetricDataRequest.start_time required")
    if "endTime" in data:
        import capo_lightsail.types.iso_date

        out["end_time"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["endTime"]
        )
    else:
        raise DeserializationError("GetBucketMetricDataRequest.end_time required")
    if "period" in data:
        out["period"] = data["period"]
    else:
        raise DeserializationError("GetBucketMetricDataRequest.period required")
    if "statistics" in data:
        import capo_lightsail.types.metric_statistic_list

        out["statistics"] = (
            capo_lightsail.types.metric_statistic_list.deserialize_aws_json_1_1(
                data["statistics"]
            )
        )
    else:
        raise DeserializationError("GetBucketMetricDataRequest.statistics required")
    if "unit" in data:
        import capo_lightsail.types.metric_unit

        out["unit"] = capo_lightsail.types.metric_unit.deserialize_aws_json_1_1(
            data["unit"]
        )
    else:
        raise DeserializationError("GetBucketMetricDataRequest.unit required")
    return out
