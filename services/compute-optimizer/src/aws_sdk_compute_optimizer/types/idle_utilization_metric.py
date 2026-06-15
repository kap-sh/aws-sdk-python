"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleUtilizationMetric``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.idle_dimensions
    import aws_sdk_compute_optimizer.types.idle_metric_name
    import aws_sdk_compute_optimizer.types.metric_statistic
    import aws_sdk_compute_optimizer.types.metric_value


class IdleUtilizationMetric(TypedDict):
    name: NotRequired["aws_sdk_compute_optimizer.types.idle_metric_name.IdleMetricName"]
    """<p>The name of the utilization metric.</p>"""
    statistic: NotRequired[
        "aws_sdk_compute_optimizer.types.metric_statistic.MetricStatistic"
    ]
    r"""<p> The statistic of the utilization metric. </p> <p>The Compute Optimizer API, Command Line Interface (CLI), and SDKs return utilization metrics using only the <code>Maximum</code> statistic, which is the highest value observed during the specified period.</p> <p>The Compute Optimizer console displays graphs for some utilization metrics using the <code>Average</code> statistic, which is the value of <code>Sum</code> / <code>SampleCount</code> during the specified period. For more information, see <a href=\"https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendations.html\">Viewing resource recommendations</a> in the <i>Compute Optimizer User Guide</i>. You can also get averaged utilization metric data for your resources using Amazon CloudWatch. For more information, see the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html\">Amazon CloudWatch User Guide</a>.</p>"""
    value: "aws_sdk_compute_optimizer.types.metric_value.MetricValue"
    """<p>The value of the utilization metric.</p>"""
    dimensions: NotRequired[
        "aws_sdk_compute_optimizer.types.idle_dimensions.IdleDimensions"
    ]
    """<p>The dimensions of the utilization metric.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleUtilizationMetric) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_compute_optimizer.types.idle_metric_name

        out["name"] = (
            aws_sdk_compute_optimizer.types.idle_metric_name.serialize_aws_json_1_0(
                value["name"]
            )
        )
    if "statistic" in value:
        import aws_sdk_compute_optimizer.types.metric_statistic

        out["statistic"] = (
            aws_sdk_compute_optimizer.types.metric_statistic.serialize_aws_json_1_0(
                value["statistic"]
            )
        )
    out["value"] = value.get("value", 0)
    if "dimensions" in value:
        import aws_sdk_compute_optimizer.types.idle_dimensions

        out["dimensions"] = (
            aws_sdk_compute_optimizer.types.idle_dimensions.serialize_aws_json_1_0(
                value["dimensions"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IdleUtilizationMetric:
    out: IdleUtilizationMetric = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_compute_optimizer.types.idle_metric_name

        out["name"] = (
            aws_sdk_compute_optimizer.types.idle_metric_name.deserialize_aws_json_1_0(
                data["name"]
            )
        )
    if "statistic" in data:
        import aws_sdk_compute_optimizer.types.metric_statistic

        out["statistic"] = (
            aws_sdk_compute_optimizer.types.metric_statistic.deserialize_aws_json_1_0(
                data["statistic"]
            )
        )
    if "value" in data:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    if "dimensions" in data:
        import aws_sdk_compute_optimizer.types.idle_dimensions

        out["dimensions"] = (
            aws_sdk_compute_optimizer.types.idle_dimensions.deserialize_aws_json_1_0(
                data["dimensions"]
            )
        )
    return out
