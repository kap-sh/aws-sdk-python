"""Generated from Smithy shape ``com.amazonaws.inspector2#Usage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.currency
    import capo_inspector2.types.monthly_cost_estimate
    import capo_inspector2.types.usage_type
    import capo_inspector2.types.usage_value


class Usage(TypedDict, closed=True):
    type: NotRequired["capo_inspector2.types.usage_type.UsageType"]
    """<p>The type scan.</p>"""
    total: "capo_inspector2.types.usage_value.UsageValue"
    """<p>The total of usage.</p>"""
    estimated_monthly_cost: (
        "capo_inspector2.types.monthly_cost_estimate.MonthlyCostEstimate"
    )
    """<p>The estimated monthly cost of Amazon Inspector.</p>"""
    currency: NotRequired["capo_inspector2.types.currency.Currency"]
    """<p>The currency type used when calculating usage data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Usage) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    out["total"] = value.get("total", 0)
    out["estimatedMonthlyCost"] = value.get("estimated_monthly_cost", 0)
    if "currency" in value:
        out["currency"] = value["currency"]
    return out


def deserialize_json(data: dict) -> Usage:
    out: Usage = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "total" in data:
        out["total"] = data["total"]
    else:
        out["total"] = 0
    if "estimatedMonthlyCost" in data:
        out["estimated_monthly_cost"] = data["estimatedMonthlyCost"]
    else:
        out["estimated_monthly_cost"] = 0
    if "currency" in data:
        out["currency"] = data["currency"]
    return out
