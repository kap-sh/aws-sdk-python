"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ReservedInstancesPricing``."""

from typing_extensions import NotRequired, TypedDict


class ReservedInstancesPricing(TypedDict, closed=True):
    estimated_on_demand_cost: NotRequired["float"]
    """<p>The remaining On-Demand cost estimated to not be covered by the recommended reserved instance, over the length of the lookback period.</p>"""
    monthly_reservation_eligible_cost: NotRequired["float"]
    """<p>The cost of paying for the recommended reserved instance monthly.</p>"""
    savings_percentage: NotRequired["float"]
    """<p>The savings percentage relative to the total On-Demand costs that are associated with this instance.</p>"""
    estimated_monthly_amortized_reservation_cost: NotRequired["float"]
    """<p>The estimated cost of your recurring monthly fees for the recommended reserved instance across the month.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReservedInstancesPricing) -> dict:
    out: dict = {}
    if "estimated_on_demand_cost" in value:
        out["estimatedOnDemandCost"] = value["estimated_on_demand_cost"]
    if "monthly_reservation_eligible_cost" in value:
        out["monthlyReservationEligibleCost"] = value[
            "monthly_reservation_eligible_cost"
        ]
    if "savings_percentage" in value:
        out["savingsPercentage"] = value["savings_percentage"]
    if "estimated_monthly_amortized_reservation_cost" in value:
        out["estimatedMonthlyAmortizedReservationCost"] = value[
            "estimated_monthly_amortized_reservation_cost"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> ReservedInstancesPricing:
    out: ReservedInstancesPricing = {}  # type: ignore[typeddict-item]
    if "estimatedOnDemandCost" in data:
        out["estimated_on_demand_cost"] = data["estimatedOnDemandCost"]
    if "monthlyReservationEligibleCost" in data:
        out["monthly_reservation_eligible_cost"] = data[
            "monthlyReservationEligibleCost"
        ]
    if "savingsPercentage" in data:
        out["savings_percentage"] = data["savingsPercentage"]
    if "estimatedMonthlyAmortizedReservationCost" in data:
        out["estimated_monthly_amortized_reservation_cost"] = data[
            "estimatedMonthlyAmortizedReservationCost"
        ]
    return out
