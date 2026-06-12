"""Generated from Smithy shape ``com.amazonaws.codebuild#ScalingConfigurationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.fleet_capacity
    import aws_sdk_codebuild.types.fleet_scaling_type
    import aws_sdk_codebuild.types.target_tracking_scaling_configurations


class ScalingConfigurationOutput(TypedDict):
    scaling_type: NotRequired[
        "aws_sdk_codebuild.types.fleet_scaling_type.FleetScalingType"
    ]
    """<p>The scaling type for a compute fleet.</p>"""
    target_tracking_scaling_configs: NotRequired[
        "aws_sdk_codebuild.types.target_tracking_scaling_configurations.TargetTrackingScalingConfigurations"
    ]
    """<p>A list of <code>TargetTrackingScalingConfiguration</code> objects.</p>"""
    max_capacity: NotRequired["aws_sdk_codebuild.types.fleet_capacity.FleetCapacity"]
    """<p>The maximum number of instances in the ﬂeet when auto-scaling.</p>"""
    desired_capacity: NotRequired[
        "aws_sdk_codebuild.types.fleet_capacity.FleetCapacity"
    ]
    """<p>The desired number of instances in the ﬂeet when auto-scaling.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingConfigurationOutput) -> dict:
    out: dict = {}
    if "scaling_type" in value:
        import aws_sdk_codebuild.types.fleet_scaling_type

        out["scalingType"] = (
            aws_sdk_codebuild.types.fleet_scaling_type.serialize_aws_json_1_1(
                value["scaling_type"]
            )
        )
    if "target_tracking_scaling_configs" in value:
        import aws_sdk_codebuild.types.target_tracking_scaling_configurations

        out["targetTrackingScalingConfigs"] = (
            aws_sdk_codebuild.types.target_tracking_scaling_configurations.serialize_aws_json_1_1(
                value["target_tracking_scaling_configs"]
            )
        )
    if "max_capacity" in value:
        out["maxCapacity"] = value["max_capacity"]
    if "desired_capacity" in value:
        out["desiredCapacity"] = value["desired_capacity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScalingConfigurationOutput:
    out: ScalingConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "scalingType" in data:
        import aws_sdk_codebuild.types.fleet_scaling_type

        out["scaling_type"] = (
            aws_sdk_codebuild.types.fleet_scaling_type.deserialize_aws_json_1_1(
                data["scalingType"]
            )
        )
    if "targetTrackingScalingConfigs" in data:
        import aws_sdk_codebuild.types.target_tracking_scaling_configurations

        out["target_tracking_scaling_configs"] = (
            aws_sdk_codebuild.types.target_tracking_scaling_configurations.deserialize_aws_json_1_1(
                data["targetTrackingScalingConfigs"]
            )
        )
    if "maxCapacity" in data:
        out["max_capacity"] = data["maxCapacity"]
    if "desiredCapacity" in data:
        out["desired_capacity"] = data["desiredCapacity"]
    return out
