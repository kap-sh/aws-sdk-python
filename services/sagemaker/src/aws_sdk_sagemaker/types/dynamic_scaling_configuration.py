"""Generated from Smithy shape ``com.amazonaws.sagemaker#DynamicScalingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.integer
    import aws_sdk_sagemaker.types.scaling_policies


class DynamicScalingConfiguration(TypedDict, closed=True):
    min_capacity: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The recommended minimum capacity to specify for your autoscaling policy.</p>"""
    max_capacity: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The recommended maximum capacity to specify for your autoscaling policy.</p>"""
    scale_in_cooldown: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The recommended scale in cooldown time for your autoscaling policy.</p>"""
    scale_out_cooldown: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The recommended scale out cooldown time for your autoscaling policy.</p>"""
    scaling_policies: NotRequired[
        "aws_sdk_sagemaker.types.scaling_policies.ScalingPolicies"
    ]
    """<p>An object of the scaling policies for each metric.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DynamicScalingConfiguration) -> dict:
    out: dict = {}
    if "min_capacity" in value:
        out["MinCapacity"] = value["min_capacity"]
    if "max_capacity" in value:
        out["MaxCapacity"] = value["max_capacity"]
    if "scale_in_cooldown" in value:
        out["ScaleInCooldown"] = value["scale_in_cooldown"]
    if "scale_out_cooldown" in value:
        out["ScaleOutCooldown"] = value["scale_out_cooldown"]
    if "scaling_policies" in value:
        import aws_sdk_sagemaker.types.scaling_policies

        out["ScalingPolicies"] = (
            aws_sdk_sagemaker.types.scaling_policies.serialize_aws_json_1_1(
                value["scaling_policies"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DynamicScalingConfiguration:
    out: DynamicScalingConfiguration = {}  # type: ignore[typeddict-item]
    if "MinCapacity" in data:
        out["min_capacity"] = data["MinCapacity"]
    if "MaxCapacity" in data:
        out["max_capacity"] = data["MaxCapacity"]
    if "ScaleInCooldown" in data:
        out["scale_in_cooldown"] = data["ScaleInCooldown"]
    if "ScaleOutCooldown" in data:
        out["scale_out_cooldown"] = data["ScaleOutCooldown"]
    if "ScalingPolicies" in data:
        import aws_sdk_sagemaker.types.scaling_policies

        out["scaling_policies"] = (
            aws_sdk_sagemaker.types.scaling_policies.deserialize_aws_json_1_1(
                data["ScalingPolicies"]
            )
        )
    return out
