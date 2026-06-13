"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#SavingsPlansPricing``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SavingsPlansPricing(TypedDict):
    monthly_savings_plans_eligible_cost: NotRequired["float"]
    """<p>The cost of paying for the recommended Savings Plans monthly.</p>"""
    estimated_monthly_commitment: NotRequired["float"]
    """<p>Estimated monthly commitment for the Savings Plans.</p>"""
    savings_percentage: NotRequired["float"]
    """<p>Estimated savings as a percentage of your overall costs after buying the Savings Plans.</p>"""
    estimated_on_demand_cost: NotRequired["float"]
    """<p>Estimated On-Demand cost you will pay after buying the Savings Plans.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SavingsPlansPricing) -> dict:
    out: dict = {}
    if "monthly_savings_plans_eligible_cost" in value:
        out["monthlySavingsPlansEligibleCost"] = value[
            "monthly_savings_plans_eligible_cost"
        ]
    if "estimated_monthly_commitment" in value:
        out["estimatedMonthlyCommitment"] = value["estimated_monthly_commitment"]
    if "savings_percentage" in value:
        out["savingsPercentage"] = value["savings_percentage"]
    if "estimated_on_demand_cost" in value:
        out["estimatedOnDemandCost"] = value["estimated_on_demand_cost"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SavingsPlansPricing:
    out: SavingsPlansPricing = {}  # type: ignore[typeddict-item]
    if "monthlySavingsPlansEligibleCost" in data:
        out["monthly_savings_plans_eligible_cost"] = data[
            "monthlySavingsPlansEligibleCost"
        ]
    if "estimatedMonthlyCommitment" in data:
        out["estimated_monthly_commitment"] = data["estimatedMonthlyCommitment"]
    if "savingsPercentage" in data:
        out["savings_percentage"] = data["savingsPercentage"]
    if "estimatedOnDemandCost" in data:
        out["estimated_on_demand_cost"] = data["estimatedOnDemandCost"]
    return out
