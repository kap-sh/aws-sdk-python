"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProductionVariantManagedInstanceScalingScaleInPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.managed_instance_scaling_cooldown_in_minutes
    import capo_sagemaker.types.managed_instance_scaling_maximum_step_size
    import capo_sagemaker.types.managed_instance_scaling_scale_in_strategy


class ProductionVariantManagedInstanceScalingScaleInPolicy(TypedDict, closed=True):
    strategy: NotRequired[
        "capo_sagemaker.types.managed_instance_scaling_scale_in_strategy.ManagedInstanceScalingScaleInStrategy"
    ]
    """<p>The strategy for scaling in instances.</p> <dl> <dt>IDLE_RELEASE</dt> <dd> <p>Releases instances that have no hosted inference component copies.</p> </dd> <dt>CONSOLIDATION</dt> <dd> <p>Consolidates inference component copies onto fewer instances to release more instances. Consolidation honors the scheduling configuration of each inference component. For example, if an inference component specifies Availability Zone balance, consolidation only proceeds when the resulting distribution does not increase the imbalance.</p> </dd> </dl>"""
    maximum_step_size: NotRequired[
        "capo_sagemaker.types.managed_instance_scaling_maximum_step_size.ManagedInstanceScalingMaximumStepSize"
    ]
    """<p>The maximum number of instances that the endpoint can terminate at a time during a consolidation scale-in operation.</p> <p>Default value: <code>1</code>.</p>"""
    cooldown_in_minutes: NotRequired[
        "capo_sagemaker.types.managed_instance_scaling_cooldown_in_minutes.ManagedInstanceScalingCooldownInMinutes"
    ]
    """<p>The cooldown period, in minutes, after the last endpoint operation before the endpoint evaluates consolidation scale-in opportunities.</p> <p>Default value: <code>20</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ProductionVariantManagedInstanceScalingScaleInPolicy,
) -> dict:
    out: dict = {}
    if "strategy" in value:
        import capo_sagemaker.types.managed_instance_scaling_scale_in_strategy

        out["Strategy"] = (
            capo_sagemaker.types.managed_instance_scaling_scale_in_strategy.serialize_aws_json_1_1(
                value["strategy"]
            )
        )
    if "maximum_step_size" in value:
        out["MaximumStepSize"] = value["maximum_step_size"]
    if "cooldown_in_minutes" in value:
        out["CooldownInMinutes"] = value["cooldown_in_minutes"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ProductionVariantManagedInstanceScalingScaleInPolicy:
    out: ProductionVariantManagedInstanceScalingScaleInPolicy = {}  # type: ignore[typeddict-item]
    if "Strategy" in data:
        import capo_sagemaker.types.managed_instance_scaling_scale_in_strategy

        out["strategy"] = (
            capo_sagemaker.types.managed_instance_scaling_scale_in_strategy.deserialize_aws_json_1_1(
                data["Strategy"]
            )
        )
    if "MaximumStepSize" in data:
        out["maximum_step_size"] = data["MaximumStepSize"]
    if "CooldownInMinutes" in data:
        out["cooldown_in_minutes"] = data["CooldownInMinutes"]
    return out
