"""Generated from Smithy shape ``com.amazonaws.dynamodb#AutoScalingPolicyDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.auto_scaling_policy_name
    import capo_dynamodb.types.auto_scaling_target_tracking_scaling_policy_configuration_description


class AutoScalingPolicyDescription(TypedDict, closed=True):
    policy_name: NotRequired[
        "capo_dynamodb.types.auto_scaling_policy_name.AutoScalingPolicyName"
    ]
    """<p>The name of the scaling policy.</p>"""
    target_tracking_scaling_policy_configuration: NotRequired[
        "capo_dynamodb.types.auto_scaling_target_tracking_scaling_policy_configuration_description.AutoScalingTargetTrackingScalingPolicyConfigurationDescription"
    ]
    """<p>Represents a target tracking scaling policy configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingPolicyDescription) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    if "target_tracking_scaling_policy_configuration" in value:
        import capo_dynamodb.types.auto_scaling_target_tracking_scaling_policy_configuration_description

        out["TargetTrackingScalingPolicyConfiguration"] = (
            capo_dynamodb.types.auto_scaling_target_tracking_scaling_policy_configuration_description.serialize_aws_json_1_0(
                value["target_tracking_scaling_policy_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutoScalingPolicyDescription:
    out: AutoScalingPolicyDescription = {}  # type: ignore[typeddict-item]
    if "PolicyName" in data:
        out["policy_name"] = data["PolicyName"]
    if "TargetTrackingScalingPolicyConfiguration" in data:
        import capo_dynamodb.types.auto_scaling_target_tracking_scaling_policy_configuration_description

        out["target_tracking_scaling_policy_configuration"] = (
            capo_dynamodb.types.auto_scaling_target_tracking_scaling_policy_configuration_description.deserialize_aws_json_1_0(
                data["TargetTrackingScalingPolicyConfiguration"]
            )
        )
    return out
