"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#CostDifference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.cost_amount


class CostDifference(TypedDict, closed=True):
    historical_cost: NotRequired[
        "capo_bcm_pricing_calculator.types.cost_amount.CostAmount"
    ]
    """<p> The historical cost amount. </p>"""
    estimated_cost: NotRequired[
        "capo_bcm_pricing_calculator.types.cost_amount.CostAmount"
    ]
    """<p> The estimated cost amount. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CostDifference) -> dict:
    out: dict = {}
    if "historical_cost" in value:
        import capo_bcm_pricing_calculator.types.cost_amount

        out["historicalCost"] = (
            capo_bcm_pricing_calculator.types.cost_amount.serialize_aws_json_1_0(
                value["historical_cost"]
            )
        )
    if "estimated_cost" in value:
        import capo_bcm_pricing_calculator.types.cost_amount

        out["estimatedCost"] = (
            capo_bcm_pricing_calculator.types.cost_amount.serialize_aws_json_1_0(
                value["estimated_cost"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CostDifference:
    out: CostDifference = {}  # type: ignore[typeddict-item]
    if "historicalCost" in data:
        import capo_bcm_pricing_calculator.types.cost_amount

        out["historical_cost"] = (
            capo_bcm_pricing_calculator.types.cost_amount.deserialize_aws_json_1_0(
                data["historicalCost"]
            )
        )
    if "estimatedCost" in data:
        import capo_bcm_pricing_calculator.types.cost_amount

        out["estimated_cost"] = (
            capo_bcm_pricing_calculator.types.cost_amount.deserialize_aws_json_1_0(
                data["estimatedCost"]
            )
        )
    return out
