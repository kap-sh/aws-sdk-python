"""Generated from Smithy shape ``com.amazonaws.codebuild#TargetTrackingScalingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.fleet_scaling_metric_type
    import aws_sdk_codebuild.types.wrapper_double


class TargetTrackingScalingConfiguration(TypedDict, closed=True):
    metric_type: NotRequired[
        "aws_sdk_codebuild.types.fleet_scaling_metric_type.FleetScalingMetricType"
    ]
    """<p>The metric type to determine auto-scaling.</p>"""
    target_value: NotRequired["aws_sdk_codebuild.types.wrapper_double.WrapperDouble"]
    """<p>The value of <code>metricType</code> when to start scaling.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetTrackingScalingConfiguration) -> dict:
    out: dict = {}
    if "metric_type" in value:
        import aws_sdk_codebuild.types.fleet_scaling_metric_type

        out["metricType"] = (
            aws_sdk_codebuild.types.fleet_scaling_metric_type.serialize_aws_json_1_1(
                value["metric_type"]
            )
        )
    if "target_value" in value:
        out["targetValue"] = value["target_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetTrackingScalingConfiguration:
    out: TargetTrackingScalingConfiguration = {}  # type: ignore[typeddict-item]
    if "metricType" in data:
        import aws_sdk_codebuild.types.fleet_scaling_metric_type

        out["metric_type"] = (
            aws_sdk_codebuild.types.fleet_scaling_metric_type.deserialize_aws_json_1_1(
                data["metricType"]
            )
        )
    if "targetValue" in data:
        out["target_value"] = data["targetValue"]
    return out
