"""Generated from Smithy shape ``com.amazonaws.sagemaker#TargetTrackingScalingPolicyConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.double
    import aws_sdk_sagemaker.types.metric_specification


class TargetTrackingScalingPolicyConfiguration(TypedDict):
    metric_specification: NotRequired[
        "aws_sdk_sagemaker.types.metric_specification.MetricSpecification"
    ]
    """<p>An object containing information about a metric.</p>"""
    target_value: NotRequired["aws_sdk_sagemaker.types.double.Double"]
    """<p>The recommended target value to specify for the metric when creating a scaling policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetTrackingScalingPolicyConfiguration) -> dict:
    out: dict = {}
    if "metric_specification" in value:
        import aws_sdk_sagemaker.types.metric_specification

        out["MetricSpecification"] = (
            aws_sdk_sagemaker.types.metric_specification.serialize_aws_json_1_1(
                value["metric_specification"]
            )
        )
    if "target_value" in value:
        out["TargetValue"] = value["target_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetTrackingScalingPolicyConfiguration:
    out: TargetTrackingScalingPolicyConfiguration = {}  # type: ignore[typeddict-item]
    if "MetricSpecification" in data:
        import aws_sdk_sagemaker.types.metric_specification

        out["metric_specification"] = (
            aws_sdk_sagemaker.types.metric_specification.deserialize_aws_json_1_1(
                data["MetricSpecification"]
            )
        )
    if "TargetValue" in data:
        out["target_value"] = data["TargetValue"]
    return out
