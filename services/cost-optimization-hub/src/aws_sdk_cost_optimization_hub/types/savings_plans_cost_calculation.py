"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#SavingsPlansCostCalculation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.savings_plans_pricing


class SavingsPlansCostCalculation(TypedDict):
    pricing: NotRequired[
        "aws_sdk_cost_optimization_hub.types.savings_plans_pricing.SavingsPlansPricing"
    ]
    """<p>Pricing details of the purchase recommendation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SavingsPlansCostCalculation) -> dict:
    out: dict = {}
    if "pricing" in value:
        import aws_sdk_cost_optimization_hub.types.savings_plans_pricing

        out["pricing"] = (
            aws_sdk_cost_optimization_hub.types.savings_plans_pricing.serialize_aws_json_1_0(
                value["pricing"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SavingsPlansCostCalculation:
    out: SavingsPlansCostCalculation = {}  # type: ignore[typeddict-item]
    if "pricing" in data:
        import aws_sdk_cost_optimization_hub.types.savings_plans_pricing

        out["pricing"] = (
            aws_sdk_cost_optimization_hub.types.savings_plans_pricing.deserialize_aws_json_1_0(
                data["pricing"]
            )
        )
    return out
