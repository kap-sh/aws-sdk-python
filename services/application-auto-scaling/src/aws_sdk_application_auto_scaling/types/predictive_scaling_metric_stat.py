"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PredictiveScalingMetricStat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.predictive_scaling_metric
    import aws_sdk_application_auto_scaling.types.predictive_scaling_metric_unit
    import aws_sdk_application_auto_scaling.types.xml_string


class PredictiveScalingMetricStat(TypedDict, closed=True):
    metric: "aws_sdk_application_auto_scaling.types.predictive_scaling_metric.PredictiveScalingMetric"
    r"""<p> The CloudWatch metric to return, including the metric name, namespace, and dimensions. To get the exact metric name, namespace, and dimensions, inspect the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Metric.html\">Metric</a> object that is returned by a call to <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html\">ListMetrics</a>. </p>"""
    stat: "aws_sdk_application_auto_scaling.types.xml_string.XmlString"
    r"""<p> The statistic to return. It can include any CloudWatch statistic or extended statistic. For a list of valid values, see the table in <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic\">Statistics</a> in the <i>Amazon CloudWatch User Guide</i>. </p> <p>The most commonly used metrics for predictive scaling are <code>Average</code> and <code>Sum</code>.</p>"""
    unit: NotRequired[
        "aws_sdk_application_auto_scaling.types.predictive_scaling_metric_unit.PredictiveScalingMetricUnit"
    ]
    r"""<p> The unit to use for the returned data points. For a complete list of the units that CloudWatch supports, see the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html\">MetricDatum</a> data type in the <i>Amazon CloudWatch API Reference</i>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictiveScalingMetricStat) -> dict:
    out: dict = {}
    import aws_sdk_application_auto_scaling.types.predictive_scaling_metric

    out["Metric"] = (
        aws_sdk_application_auto_scaling.types.predictive_scaling_metric.serialize_aws_json_1_1(
            value["metric"]
        )
    )
    out["Stat"] = value["stat"]
    if "unit" in value:
        out["Unit"] = value["unit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictiveScalingMetricStat:
    out: PredictiveScalingMetricStat = {}  # type: ignore[typeddict-item]
    if "Metric" in data:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_metric

        out["metric"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_metric.deserialize_aws_json_1_1(
                data["Metric"]
            )
        )
    else:
        raise DeserializationError("PredictiveScalingMetricStat.metric required")
    if "Stat" in data:
        out["stat"] = data["Stat"]
    else:
        raise DeserializationError("PredictiveScalingMetricStat.stat required")
    if "Unit" in data:
        out["unit"] = data["Unit"]
    return out
