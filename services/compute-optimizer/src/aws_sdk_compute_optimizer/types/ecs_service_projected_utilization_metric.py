"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceProjectedUtilizationMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.ecs_service_metric_name
    import aws_sdk_compute_optimizer.types.ecs_service_metric_statistic
    import aws_sdk_compute_optimizer.types.lower_bound_value
    import aws_sdk_compute_optimizer.types.upper_bound_value


class ECSServiceProjectedUtilizationMetric(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_compute_optimizer.types.ecs_service_metric_name.ECSServiceMetricName"
    ]
    """<p> The name of the projected utilization metric. </p> <p>The following utilization metrics are available:</p> <ul> <li> <p> <code>Cpu</code> — The percentage of allocated compute units that are currently in use on the service tasks.</p> </li> <li> <p> <code>Memory</code> — The percentage of memory that's currently in use on the service tasks.</p> </li> </ul>"""
    statistic: NotRequired[
        "aws_sdk_compute_optimizer.types.ecs_service_metric_statistic.ECSServiceMetricStatistic"
    ]
    r"""<p>The statistic of the projected utilization metric.</p> <p>The Compute Optimizer API, Command Line Interface (CLI), and SDKs return utilization metrics using only the <code>Maximum</code> statistic, which is the highest value observed during the specified period.</p> <p>The Compute Optimizer console displays graphs for some utilization metrics using the <code>Average</code> statistic, which is the value of <code>Sum</code> / <code>SampleCount</code> during the specified period. For more information, see <a href=\"https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendations.html\">Viewing resource recommendations</a> in the <i>Compute Optimizer User Guide</i>. You can also get averaged utilization metric data for your resources using Amazon CloudWatch. For more information, see the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html\">Amazon CloudWatch User Guide</a>.</p>"""
    lower_bound_value: (
        "aws_sdk_compute_optimizer.types.lower_bound_value.LowerBoundValue"
    )
    """<p> The lower bound values for the projected utilization metrics. </p>"""
    upper_bound_value: (
        "aws_sdk_compute_optimizer.types.upper_bound_value.UpperBoundValue"
    )
    """<p> The upper bound values for the projected utilization metrics. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceProjectedUtilizationMetric) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_compute_optimizer.types.ecs_service_metric_name

        out["name"] = (
            aws_sdk_compute_optimizer.types.ecs_service_metric_name.serialize_aws_json_1_0(
                value["name"]
            )
        )
    if "statistic" in value:
        import aws_sdk_compute_optimizer.types.ecs_service_metric_statistic

        out["statistic"] = (
            aws_sdk_compute_optimizer.types.ecs_service_metric_statistic.serialize_aws_json_1_0(
                value["statistic"]
            )
        )
    out["lowerBoundValue"] = value.get("lower_bound_value", 0)
    out["upperBoundValue"] = value.get("upper_bound_value", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> ECSServiceProjectedUtilizationMetric:
    out: ECSServiceProjectedUtilizationMetric = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_compute_optimizer.types.ecs_service_metric_name

        out["name"] = (
            aws_sdk_compute_optimizer.types.ecs_service_metric_name.deserialize_aws_json_1_0(
                data["name"]
            )
        )
    if "statistic" in data:
        import aws_sdk_compute_optimizer.types.ecs_service_metric_statistic

        out["statistic"] = (
            aws_sdk_compute_optimizer.types.ecs_service_metric_statistic.deserialize_aws_json_1_0(
                data["statistic"]
            )
        )
    if "lowerBoundValue" in data:
        out["lower_bound_value"] = data["lowerBoundValue"]
    else:
        out["lower_bound_value"] = 0
    if "upperBoundValue" in data:
        out["upper_bound_value"] = data["upperBoundValue"]
    else:
        out["upper_bound_value"] = 0
    return out
