"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#EstimatedDiscounts``."""

from typing_extensions import NotRequired, TypedDict


class EstimatedDiscounts(TypedDict, closed=True):
    savings_plans_discount: NotRequired["float"]
    """<p>Estimated Savings Plans discounts.</p>"""
    reserved_instances_discount: NotRequired["float"]
    """<p>Estimated reserved instance discounts.</p>"""
    other_discount: NotRequired["float"]
    """<p>Estimated other discounts include all discounts that are not itemized. Itemized discounts include <code>reservedInstanceDiscount</code> and <code>savingsPlansDiscount</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EstimatedDiscounts) -> dict:
    out: dict = {}
    if "savings_plans_discount" in value:
        out["savingsPlansDiscount"] = value["savings_plans_discount"]
    if "reserved_instances_discount" in value:
        out["reservedInstancesDiscount"] = value["reserved_instances_discount"]
    if "other_discount" in value:
        out["otherDiscount"] = value["other_discount"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EstimatedDiscounts:
    out: EstimatedDiscounts = {}  # type: ignore[typeddict-item]
    if "savingsPlansDiscount" in data:
        out["savings_plans_discount"] = data["savingsPlansDiscount"]
    if "reservedInstancesDiscount" in data:
        out["reserved_instances_discount"] = data["reservedInstancesDiscount"]
    if "otherDiscount" in data:
        out["other_discount"] = data["otherDiscount"]
    return out
