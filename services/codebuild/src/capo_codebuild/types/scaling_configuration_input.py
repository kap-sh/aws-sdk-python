"""Generated from Smithy shape ``com.amazonaws.codebuild#ScalingConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.fleet_capacity
    import capo_codebuild.types.fleet_scaling_type
    import capo_codebuild.types.target_tracking_scaling_configurations


class ScalingConfigurationInput(TypedDict, closed=True):
    scaling_type: NotRequired[
        "capo_codebuild.types.fleet_scaling_type.FleetScalingType"
    ]
    """<p>The scaling type for a compute fleet.</p>"""
    target_tracking_scaling_configs: NotRequired[
        "capo_codebuild.types.target_tracking_scaling_configurations.TargetTrackingScalingConfigurations"
    ]
    """<p>A list of <code>TargetTrackingScalingConfiguration</code> objects.</p>"""
    max_capacity: NotRequired["capo_codebuild.types.fleet_capacity.FleetCapacity"]
    """<p>The maximum number of instances in the ﬂeet when auto-scaling.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingConfigurationInput) -> dict:
    out: dict = {}
    if "scaling_type" in value:
        import capo_codebuild.types.fleet_scaling_type

        out["scalingType"] = (
            capo_codebuild.types.fleet_scaling_type.serialize_aws_json_1_1(
                value["scaling_type"]
            )
        )
    if "target_tracking_scaling_configs" in value:
        import capo_codebuild.types.target_tracking_scaling_configurations

        out["targetTrackingScalingConfigs"] = (
            capo_codebuild.types.target_tracking_scaling_configurations.serialize_aws_json_1_1(
                value["target_tracking_scaling_configs"]
            )
        )
    if "max_capacity" in value:
        out["maxCapacity"] = value["max_capacity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScalingConfigurationInput:
    out: ScalingConfigurationInput = {}  # type: ignore[typeddict-item]
    if "scalingType" in data:
        import capo_codebuild.types.fleet_scaling_type

        out["scaling_type"] = (
            capo_codebuild.types.fleet_scaling_type.deserialize_aws_json_1_1(
                data["scalingType"]
            )
        )
    if "targetTrackingScalingConfigs" in data:
        import capo_codebuild.types.target_tracking_scaling_configurations

        out["target_tracking_scaling_configs"] = (
            capo_codebuild.types.target_tracking_scaling_configurations.deserialize_aws_json_1_1(
                data["targetTrackingScalingConfigs"]
            )
        )
    if "maxCapacity" in data:
        out["max_capacity"] = data["maxCapacity"]
    return out
