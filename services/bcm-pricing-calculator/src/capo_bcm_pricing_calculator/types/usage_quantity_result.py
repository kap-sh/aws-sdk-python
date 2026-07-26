"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#UsageQuantityResult``."""

from typing_extensions import NotRequired, TypedDict


class UsageQuantityResult(TypedDict, closed=True):
    amount: NotRequired["float"]
    """<p> The numeric value of the usage quantity result. </p>"""
    unit: NotRequired["str"]
    """<p> The unit of measurement for the usage quantity result. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UsageQuantityResult) -> dict:
    out: dict = {}
    if "amount" in value:
        out["amount"] = value["amount"]
    if "unit" in value:
        out["unit"] = value["unit"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UsageQuantityResult:
    out: UsageQuantityResult = {}  # type: ignore[typeddict-item]
    if "amount" in data:
        out["amount"] = data["amount"]
    if "unit" in data:
        out["unit"] = data["unit"]
    return out
