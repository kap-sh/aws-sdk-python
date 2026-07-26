"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansCoverageData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string


class SavingsPlansCoverageData(TypedDict, closed=True):
    spend_covered_by_savings_plans: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The amount of your Amazon Web Services usage that's covered by a Savings Plans.</p>"""
    on_demand_cost: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The cost of your Amazon Web Services usage at the public On-Demand rate.</p>"""
    total_cost: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The total cost of your Amazon Web Services usage, regardless of your purchase option.</p>"""
    coverage_percentage: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The percentage of your existing Savings Plans covered usage, divided by all of your eligible Savings Plans usage in an account (or set of accounts).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansCoverageData) -> dict:
    out: dict = {}
    if "spend_covered_by_savings_plans" in value:
        out["SpendCoveredBySavingsPlans"] = value["spend_covered_by_savings_plans"]
    if "on_demand_cost" in value:
        out["OnDemandCost"] = value["on_demand_cost"]
    if "total_cost" in value:
        out["TotalCost"] = value["total_cost"]
    if "coverage_percentage" in value:
        out["CoveragePercentage"] = value["coverage_percentage"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SavingsPlansCoverageData:
    out: SavingsPlansCoverageData = {}  # type: ignore[typeddict-item]
    if "SpendCoveredBySavingsPlans" in data:
        out["spend_covered_by_savings_plans"] = data["SpendCoveredBySavingsPlans"]
    if "OnDemandCost" in data:
        out["on_demand_cost"] = data["OnDemandCost"]
    if "TotalCost" in data:
        out["total_cost"] = data["TotalCost"]
    if "CoveragePercentage" in data:
        out["coverage_percentage"] = data["CoveragePercentage"]
    return out
