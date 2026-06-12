"""Generated from Smithy shape ``com.amazonaws.autoscaling#TargetTrackingMetricStat``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.metric
    import aws_sdk_auto_scaling.types.metric_granularity_in_seconds
    import aws_sdk_auto_scaling.types.metric_unit
    import aws_sdk_auto_scaling.types.xml_string_metric_stat


class TargetTrackingMetricStat(TypedDict):
    metric: NotRequired["aws_sdk_auto_scaling.types.metric.Metric"]
    """<p>The metric to use.</p>"""
    stat: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_metric_stat.XmlStringMetricStat"
    ]
    """<p>The statistic to return. It can include any CloudWatch statistic or extended statistic. For a list of valid values, see the table in <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic\">Statistics</a> in the <i>Amazon CloudWatch User Guide</i>.</p> <p>The most commonly used metric for scaling is <code>Average</code>.</p>"""
    unit: NotRequired["aws_sdk_auto_scaling.types.metric_unit.MetricUnit"]
    """<p>The unit to use for the returned data points. For a complete list of the units that CloudWatch supports, see the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html\">MetricDatum</a> data type in the <i>Amazon CloudWatch API Reference</i>.</p>"""
    period: NotRequired[
        "aws_sdk_auto_scaling.types.metric_granularity_in_seconds.MetricGranularityInSeconds"
    ]
    """<p> The period of the metric in seconds. The default value is 60. Accepted values are 10, 30, and 60. For high resolution metric, set the value to less than 60. For more information, see <a href=\"https://docs.aws.amazon.com/autoscaling/ec2/userguide/policy-creating-high-resolution-metrics.html\">Create a target tracking policy using high-resolution metrics for faster response</a>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetTrackingMetricStat, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "metric" in value:
        import aws_sdk_auto_scaling.types.metric

        aws_sdk_auto_scaling.types.metric.serialize_query(
            value["metric"], pairs, f"{prefix}.Metric"
        )
    if "stat" in value:
        pairs.append((f"{prefix}.Stat", str(value["stat"])))
    if "unit" in value:
        pairs.append((f"{prefix}.Unit", str(value["unit"])))
    if "period" in value:
        pairs.append((f"{prefix}.Period", str(value["period"])))


def deserialize_query(el: Element) -> TargetTrackingMetricStat:
    out: TargetTrackingMetricStat = {}  # type: ignore[typeddict-item]
    child_metric = el.find("Metric")
    if child_metric is not None:
        import aws_sdk_auto_scaling.types.metric

        out["metric"] = aws_sdk_auto_scaling.types.metric.deserialize_query(
            child_metric
        )
    child_stat = el.find("Stat")
    if child_stat is not None:
        out["stat"] = str(child_stat.text or "")
    child_unit = el.find("Unit")
    if child_unit is not None:
        out["unit"] = str(child_unit.text or "")
    child_period = el.find("Period")
    if child_period is not None:
        out["period"] = int(child_period.text or "")
    return out
