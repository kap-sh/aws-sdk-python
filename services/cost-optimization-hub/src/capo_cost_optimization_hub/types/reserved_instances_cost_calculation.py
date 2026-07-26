"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ReservedInstancesCostCalculation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.reserved_instances_pricing


class ReservedInstancesCostCalculation(TypedDict, closed=True):
    pricing: NotRequired[
        "capo_cost_optimization_hub.types.reserved_instances_pricing.ReservedInstancesPricing"
    ]
    """<p>Pricing details of the purchase recommendation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReservedInstancesCostCalculation) -> dict:
    out: dict = {}
    if "pricing" in value:
        import capo_cost_optimization_hub.types.reserved_instances_pricing

        out["pricing"] = (
            capo_cost_optimization_hub.types.reserved_instances_pricing.serialize_aws_json_1_0(
                value["pricing"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReservedInstancesCostCalculation:
    out: ReservedInstancesCostCalculation = {}  # type: ignore[typeddict-item]
    if "pricing" in data:
        import capo_cost_optimization_hub.types.reserved_instances_pricing

        out["pricing"] = (
            capo_cost_optimization_hub.types.reserved_instances_pricing.deserialize_aws_json_1_0(
                data["pricing"]
            )
        )
    return out
