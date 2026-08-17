"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedAutoScaling``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.managed_application_auto_scaling_policies
    import capo_ecs.types.managed_scalable_target


class ManagedAutoScaling(TypedDict, closed=True):
    scalable_target: NotRequired[
        "capo_ecs.types.managed_scalable_target.ManagedScalableTarget"
    ]
    """<p>Represents a scalable target.</p>"""
    application_auto_scaling_policies: NotRequired[
        "capo_ecs.types.managed_application_auto_scaling_policies.ManagedApplicationAutoScalingPolicies"
    ]
    """<p>The policy used for auto scaling.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedAutoScaling) -> dict:
    out: dict = {}
    if "scalable_target" in value:
        import capo_ecs.types.managed_scalable_target

        out["scalableTarget"] = (
            capo_ecs.types.managed_scalable_target.serialize_aws_json_1_1(
                value["scalable_target"]
            )
        )
    if "application_auto_scaling_policies" in value:
        import capo_ecs.types.managed_application_auto_scaling_policies

        out["applicationAutoScalingPolicies"] = (
            capo_ecs.types.managed_application_auto_scaling_policies.serialize_aws_json_1_1(
                value["application_auto_scaling_policies"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedAutoScaling:
    out: ManagedAutoScaling = {}  # type: ignore[typeddict-item]
    if data.get("scalableTarget") is not None:
        import capo_ecs.types.managed_scalable_target

        out["scalable_target"] = (
            capo_ecs.types.managed_scalable_target.deserialize_aws_json_1_1(
                data["scalableTarget"]
            )
        )
    if data.get("applicationAutoScalingPolicies") is not None:
        import capo_ecs.types.managed_application_auto_scaling_policies

        out["application_auto_scaling_policies"] = (
            capo_ecs.types.managed_application_auto_scaling_policies.deserialize_aws_json_1_1(
                data["applicationAutoScalingPolicies"]
            )
        )
    return out
