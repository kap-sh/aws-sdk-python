"""Generated from Smithy shape ``com.amazonaws.devopsguru#CloudWatchMetricsDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.cloud_watch_metrics_data_summary
    import aws_sdk_devops_guru.types.cloud_watch_metrics_dimensions
    import aws_sdk_devops_guru.types.cloud_watch_metrics_metric_name
    import aws_sdk_devops_guru.types.cloud_watch_metrics_namespace
    import aws_sdk_devops_guru.types.cloud_watch_metrics_period
    import aws_sdk_devops_guru.types.cloud_watch_metrics_stat
    import aws_sdk_devops_guru.types.cloud_watch_metrics_unit


class CloudWatchMetricsDetail(TypedDict, closed=True):
    metric_name: NotRequired[
        "aws_sdk_devops_guru.types.cloud_watch_metrics_metric_name.CloudWatchMetricsMetricName"
    ]
    """<p> The name of the CloudWatch metric. </p>"""
    namespace: NotRequired[
        "aws_sdk_devops_guru.types.cloud_watch_metrics_namespace.CloudWatchMetricsNamespace"
    ]
    """<p> The namespace of the CloudWatch metric. A namespace is a container for CloudWatch metrics. </p>"""
    dimensions: NotRequired[
        "aws_sdk_devops_guru.types.cloud_watch_metrics_dimensions.CloudWatchMetricsDimensions"
    ]
    """<p> An array of CloudWatch dimensions associated with </p>"""
    stat: NotRequired[
        "aws_sdk_devops_guru.types.cloud_watch_metrics_stat.CloudWatchMetricsStat"
    ]
    r"""<p> The type of statistic associated with the CloudWatch metric. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic\">Statistics</a> in the <i>Amazon CloudWatch User Guide</i>. </p>"""
    unit: NotRequired[
        "aws_sdk_devops_guru.types.cloud_watch_metrics_unit.CloudWatchMetricsUnit"
    ]
    """<p> The unit of measure used for the CloudWatch metric. For example, <code>Bytes</code>, <code>Seconds</code>, <code>Count</code>, and <code>Percent</code>. </p>"""
    period: (
        "aws_sdk_devops_guru.types.cloud_watch_metrics_period.CloudWatchMetricsPeriod"
    )
    """<p> The length of time associated with the CloudWatch metric in number of seconds. </p>"""
    metric_data_summary: NotRequired[
        "aws_sdk_devops_guru.types.cloud_watch_metrics_data_summary.CloudWatchMetricsDataSummary"
    ]
    """<p>This object returns anomaly metric data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchMetricsDetail) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "dimensions" in value:
        import aws_sdk_devops_guru.types.cloud_watch_metrics_dimensions

        out["Dimensions"] = (
            aws_sdk_devops_guru.types.cloud_watch_metrics_dimensions.serialize_json(
                value["dimensions"]
            )
        )
    if "stat" in value:
        import aws_sdk_devops_guru.types.cloud_watch_metrics_stat

        out["Stat"] = aws_sdk_devops_guru.types.cloud_watch_metrics_stat.serialize_json(
            value["stat"]
        )
    if "unit" in value:
        out["Unit"] = value["unit"]
    out["Period"] = value.get("period", 0)
    if "metric_data_summary" in value:
        import aws_sdk_devops_guru.types.cloud_watch_metrics_data_summary

        out["MetricDataSummary"] = (
            aws_sdk_devops_guru.types.cloud_watch_metrics_data_summary.serialize_json(
                value["metric_data_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> CloudWatchMetricsDetail:
    out: CloudWatchMetricsDetail = {}  # type: ignore[typeddict-item]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    if "Dimensions" in data:
        import aws_sdk_devops_guru.types.cloud_watch_metrics_dimensions

        out["dimensions"] = (
            aws_sdk_devops_guru.types.cloud_watch_metrics_dimensions.deserialize_json(
                data["Dimensions"]
            )
        )
    if "Stat" in data:
        import aws_sdk_devops_guru.types.cloud_watch_metrics_stat

        out["stat"] = (
            aws_sdk_devops_guru.types.cloud_watch_metrics_stat.deserialize_json(
                data["Stat"]
            )
        )
    if "Unit" in data:
        out["unit"] = data["Unit"]
    if "Period" in data:
        out["period"] = data["Period"]
    else:
        out["period"] = 0
    if "MetricDataSummary" in data:
        import aws_sdk_devops_guru.types.cloud_watch_metrics_data_summary

        out["metric_data_summary"] = (
            aws_sdk_devops_guru.types.cloud_watch_metrics_data_summary.deserialize_json(
                data["MetricDataSummary"]
            )
        )
    return out
