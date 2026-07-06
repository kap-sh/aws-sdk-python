"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#WorkloadEstimateUsageQuantity``."""

from typing_extensions import NotRequired, TypedDict


class WorkloadEstimateUsageQuantity(TypedDict, closed=True):
    unit: NotRequired["str"]
    """<p> The unit of measurement for the usage quantity. </p>"""
    amount: NotRequired["float"]
    """<p> The numeric value of the usage quantity. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkloadEstimateUsageQuantity) -> dict:
    out: dict = {}
    if "unit" in value:
        out["unit"] = value["unit"]
    if "amount" in value:
        out["amount"] = value["amount"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkloadEstimateUsageQuantity:
    out: WorkloadEstimateUsageQuantity = {}  # type: ignore[typeddict-item]
    if "unit" in data:
        out["unit"] = data["unit"]
    if "amount" in data:
        out["amount"] = data["amount"]
    return out
