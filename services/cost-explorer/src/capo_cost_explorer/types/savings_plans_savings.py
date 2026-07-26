"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansSavings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string


class SavingsPlansSavings(TypedDict, closed=True):
    net_savings: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The savings amount that you're accumulating for the usage that's covered by a Savings Plans, when compared to the On-Demand equivalent of the same usage.</p>"""
    on_demand_cost_equivalent: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>How much the amount that the usage would have cost if it was accrued at the On-Demand rate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansSavings) -> dict:
    out: dict = {}
    if "net_savings" in value:
        out["NetSavings"] = value["net_savings"]
    if "on_demand_cost_equivalent" in value:
        out["OnDemandCostEquivalent"] = value["on_demand_cost_equivalent"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SavingsPlansSavings:
    out: SavingsPlansSavings = {}  # type: ignore[typeddict-item]
    if "NetSavings" in data:
        out["net_savings"] = data["NetSavings"]
    if "OnDemandCostEquivalent" in data:
        out["on_demand_cost_equivalent"] = data["OnDemandCostEquivalent"]
    return out
