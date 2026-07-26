"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentSchedulingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_component_availability_zone_balance
    import capo_sagemaker.types.inference_component_placement_strategy


class InferenceComponentSchedulingConfig(TypedDict, closed=True):
    placement_strategy: NotRequired[
        "capo_sagemaker.types.inference_component_placement_strategy.InferenceComponentPlacementStrategy"
    ]
    """<p>The strategy for placing inference component copies across available instances. If you also set <code>AvailabilityZoneBalance</code>, this strategy applies to placement within each Availability Zone.</p> <dl> <dt>SPREAD</dt> <dd> <p>Distributes copies evenly across available instances for better resilience.</p> </dd> <dt>BINPACK</dt> <dd> <p>Packs copies onto fewer instances to optimize resource utilization.</p> </dd> </dl>"""
    availability_zone_balance: NotRequired[
        "capo_sagemaker.types.inference_component_availability_zone_balance.InferenceComponentAvailabilityZoneBalance"
    ]
    """<p>Configuration for balancing inference component copies across Availability Zones.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentSchedulingConfig) -> dict:
    out: dict = {}
    if "placement_strategy" in value:
        import capo_sagemaker.types.inference_component_placement_strategy

        out["PlacementStrategy"] = (
            capo_sagemaker.types.inference_component_placement_strategy.serialize_aws_json_1_1(
                value["placement_strategy"]
            )
        )
    if "availability_zone_balance" in value:
        import capo_sagemaker.types.inference_component_availability_zone_balance

        out["AvailabilityZoneBalance"] = (
            capo_sagemaker.types.inference_component_availability_zone_balance.serialize_aws_json_1_1(
                value["availability_zone_balance"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceComponentSchedulingConfig:
    out: InferenceComponentSchedulingConfig = {}  # type: ignore[typeddict-item]
    if "PlacementStrategy" in data:
        import capo_sagemaker.types.inference_component_placement_strategy

        out["placement_strategy"] = (
            capo_sagemaker.types.inference_component_placement_strategy.deserialize_aws_json_1_1(
                data["PlacementStrategy"]
            )
        )
    if "AvailabilityZoneBalance" in data:
        import capo_sagemaker.types.inference_component_availability_zone_balance

        out["availability_zone_balance"] = (
            capo_sagemaker.types.inference_component_availability_zone_balance.deserialize_aws_json_1_1(
                data["AvailabilityZoneBalance"]
            )
        )
    return out
