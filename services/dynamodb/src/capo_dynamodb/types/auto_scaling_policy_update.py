"""Generated from Smithy shape ``com.amazonaws.dynamodb#AutoScalingPolicyUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.auto_scaling_policy_name
    import capo_dynamodb.types.auto_scaling_target_tracking_scaling_policy_configuration_update


class AutoScalingPolicyUpdate(TypedDict, closed=True):
    policy_name: NotRequired[
        "capo_dynamodb.types.auto_scaling_policy_name.AutoScalingPolicyName"
    ]
    """<p>The name of the scaling policy.</p>"""
    target_tracking_scaling_policy_configuration: "capo_dynamodb.types.auto_scaling_target_tracking_scaling_policy_configuration_update.AutoScalingTargetTrackingScalingPolicyConfigurationUpdate"
    """<p>Represents a target tracking scaling policy configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingPolicyUpdate) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    import capo_dynamodb.types.auto_scaling_target_tracking_scaling_policy_configuration_update

    out["TargetTrackingScalingPolicyConfiguration"] = (
        capo_dynamodb.types.auto_scaling_target_tracking_scaling_policy_configuration_update.serialize_aws_json_1_0(
            value["target_tracking_scaling_policy_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutoScalingPolicyUpdate:
    out: AutoScalingPolicyUpdate = {}  # type: ignore[typeddict-item]
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    if data.get("TargetTrackingScalingPolicyConfiguration") is not None:
        import capo_dynamodb.types.auto_scaling_target_tracking_scaling_policy_configuration_update

        out["target_tracking_scaling_policy_configuration"] = (
            capo_dynamodb.types.auto_scaling_target_tracking_scaling_policy_configuration_update.deserialize_aws_json_1_0(
                data["TargetTrackingScalingPolicyConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "AutoScalingPolicyUpdate.target_tracking_scaling_policy_configuration required"
        )
    return out
