"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PredictiveScalingMetric``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.predictive_scaling_metric_dimensions
    import aws_sdk_application_auto_scaling.types.predictive_scaling_metric_name
    import aws_sdk_application_auto_scaling.types.predictive_scaling_metric_namespace


class PredictiveScalingMetric(TypedDict):
    dimensions: NotRequired[
        "aws_sdk_application_auto_scaling.types.predictive_scaling_metric_dimensions.PredictiveScalingMetricDimensions"
    ]
    """<p> Describes the dimensions of the metric. </p>"""
    metric_name: NotRequired[
        "aws_sdk_application_auto_scaling.types.predictive_scaling_metric_name.PredictiveScalingMetricName"
    ]
    """<p> The name of the metric. </p>"""
    namespace: NotRequired[
        "aws_sdk_application_auto_scaling.types.predictive_scaling_metric_namespace.PredictiveScalingMetricNamespace"
    ]
    """<p> The namespace of the metric. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictiveScalingMetric) -> dict:
    out: dict = {}
    if "dimensions" in value:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_metric_dimensions

        out["Dimensions"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_metric_dimensions.serialize_aws_json_1_1(
                value["dimensions"]
            )
        )
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictiveScalingMetric:
    out: PredictiveScalingMetric = {}  # type: ignore[typeddict-item]
    if "Dimensions" in data:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_metric_dimensions

        out["dimensions"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_metric_dimensions.deserialize_aws_json_1_1(
                data["Dimensions"]
            )
        )
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    return out
