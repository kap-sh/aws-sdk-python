"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ResourceCostCalculation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.resource_pricing
    import capo_cost_optimization_hub.types.usage_list


class ResourceCostCalculation(TypedDict, closed=True):
    usages: NotRequired["capo_cost_optimization_hub.types.usage_list.UsageList"]
    """<p>Usage details of the resource recommendation.</p>"""
    pricing: NotRequired[
        "capo_cost_optimization_hub.types.resource_pricing.ResourcePricing"
    ]
    """<p>Pricing details of the resource recommendation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceCostCalculation) -> dict:
    out: dict = {}
    if "usages" in value:
        import capo_cost_optimization_hub.types.usage_list

        out["usages"] = (
            capo_cost_optimization_hub.types.usage_list.serialize_aws_json_1_0(
                value["usages"]
            )
        )
    if "pricing" in value:
        import capo_cost_optimization_hub.types.resource_pricing

        out["pricing"] = (
            capo_cost_optimization_hub.types.resource_pricing.serialize_aws_json_1_0(
                value["pricing"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceCostCalculation:
    out: ResourceCostCalculation = {}  # type: ignore[typeddict-item]
    if "usages" in data:
        import capo_cost_optimization_hub.types.usage_list

        out["usages"] = (
            capo_cost_optimization_hub.types.usage_list.deserialize_aws_json_1_0(
                data["usages"]
            )
        )
    if "pricing" in data:
        import capo_cost_optimization_hub.types.resource_pricing

        out["pricing"] = (
            capo_cost_optimization_hub.types.resource_pricing.deserialize_aws_json_1_0(
                data["pricing"]
            )
        )
    return out
