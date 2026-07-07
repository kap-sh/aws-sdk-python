"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalingPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling_plans.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auto_scaling_plans.types.policy_name
    import aws_sdk_auto_scaling_plans.types.policy_type
    import aws_sdk_auto_scaling_plans.types.target_tracking_configuration


class ScalingPolicy(TypedDict, closed=True):
    policy_name: "aws_sdk_auto_scaling_plans.types.policy_name.PolicyName"
    """<p>The name of the scaling policy.</p>"""
    policy_type: "aws_sdk_auto_scaling_plans.types.policy_type.PolicyType"
    """<p>The type of scaling policy.</p>"""
    target_tracking_configuration: NotRequired[
        "aws_sdk_auto_scaling_plans.types.target_tracking_configuration.TargetTrackingConfiguration"
    ]
    """<p>The target tracking scaling policy. Includes support for predefined or customized metrics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingPolicy) -> dict:
    out: dict = {}
    out["PolicyName"] = value["policy_name"]
    import aws_sdk_auto_scaling_plans.types.policy_type

    out["PolicyType"] = (
        aws_sdk_auto_scaling_plans.types.policy_type.serialize_aws_json_1_1(
            value["policy_type"]
        )
    )
    if "target_tracking_configuration" in value:
        import aws_sdk_auto_scaling_plans.types.target_tracking_configuration

        out["TargetTrackingConfiguration"] = (
            aws_sdk_auto_scaling_plans.types.target_tracking_configuration.serialize_aws_json_1_1(
                value["target_tracking_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScalingPolicy:
    out: ScalingPolicy = {}  # type: ignore[typeddict-item]
    if "PolicyName" in data:
        out["policy_name"] = data["PolicyName"]
    else:
        raise DeserializationError("ScalingPolicy.policy_name required")
    if "PolicyType" in data:
        import aws_sdk_auto_scaling_plans.types.policy_type

        out["policy_type"] = (
            aws_sdk_auto_scaling_plans.types.policy_type.deserialize_aws_json_1_1(
                data["PolicyType"]
            )
        )
    else:
        raise DeserializationError("ScalingPolicy.policy_type required")
    if "TargetTrackingConfiguration" in data:
        import aws_sdk_auto_scaling_plans.types.target_tracking_configuration

        out["target_tracking_configuration"] = (
            aws_sdk_auto_scaling_plans.types.target_tracking_configuration.deserialize_aws_json_1_1(
                data["TargetTrackingConfiguration"]
            )
        )
    return out
