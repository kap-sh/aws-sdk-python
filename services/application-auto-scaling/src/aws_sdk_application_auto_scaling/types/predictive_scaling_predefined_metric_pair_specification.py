"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PredictiveScalingPredefinedMetricPairSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.predictive_scaling_metric_type
    import aws_sdk_application_auto_scaling.types.resource_label


class PredictiveScalingPredefinedMetricPairSpecification(TypedDict, closed=True):
    predefined_metric_type: "aws_sdk_application_auto_scaling.types.predictive_scaling_metric_type.PredictiveScalingMetricType"
    """<p> Indicates which metrics to use. There are two different types of metrics for each metric type: one is a load metric and one is a scaling metric. </p>"""
    resource_label: NotRequired[
        "aws_sdk_application_auto_scaling.types.resource_label.ResourceLabel"
    ]
    """<p> A label that uniquely identifies a specific target group from which to determine the total and average request count. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: PredictiveScalingPredefinedMetricPairSpecification,
) -> dict:
    out: dict = {}
    out["PredefinedMetricType"] = value["predefined_metric_type"]
    if "resource_label" in value:
        out["ResourceLabel"] = value["resource_label"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> PredictiveScalingPredefinedMetricPairSpecification:
    out: PredictiveScalingPredefinedMetricPairSpecification = {}  # type: ignore[typeddict-item]
    if "PredefinedMetricType" in data:
        out["predefined_metric_type"] = data["PredefinedMetricType"]
    else:
        raise DeserializationError(
            "PredictiveScalingPredefinedMetricPairSpecification.predefined_metric_type required"
        )
    if "ResourceLabel" in data:
        out["resource_label"] = data["ResourceLabel"]
    return out
