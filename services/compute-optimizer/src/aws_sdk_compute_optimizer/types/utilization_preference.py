"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#UtilizationPreference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.customizable_metric_name
    import aws_sdk_compute_optimizer.types.customizable_metric_parameters


class UtilizationPreference(TypedDict, closed=True):
    metric_name: NotRequired[
        "aws_sdk_compute_optimizer.types.customizable_metric_name.CustomizableMetricName"
    ]
    """<p> The name of the resource utilization metric name to customize. </p>"""
    metric_parameters: NotRequired[
        "aws_sdk_compute_optimizer.types.customizable_metric_parameters.CustomizableMetricParameters"
    ]
    """<p> The parameters to set when customizing the resource utilization thresholds. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UtilizationPreference) -> dict:
    out: dict = {}
    if "metric_name" in value:
        import aws_sdk_compute_optimizer.types.customizable_metric_name

        out["metricName"] = (
            aws_sdk_compute_optimizer.types.customizable_metric_name.serialize_aws_json_1_0(
                value["metric_name"]
            )
        )
    if "metric_parameters" in value:
        import aws_sdk_compute_optimizer.types.customizable_metric_parameters

        out["metricParameters"] = (
            aws_sdk_compute_optimizer.types.customizable_metric_parameters.serialize_aws_json_1_0(
                value["metric_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UtilizationPreference:
    out: UtilizationPreference = {}  # type: ignore[typeddict-item]
    if "metricName" in data:
        import aws_sdk_compute_optimizer.types.customizable_metric_name

        out["metric_name"] = (
            aws_sdk_compute_optimizer.types.customizable_metric_name.deserialize_aws_json_1_0(
                data["metricName"]
            )
        )
    if "metricParameters" in data:
        import aws_sdk_compute_optimizer.types.customizable_metric_parameters

        out["metric_parameters"] = (
            aws_sdk_compute_optimizer.types.customizable_metric_parameters.deserialize_aws_json_1_0(
                data["metricParameters"]
            )
        )
    return out
