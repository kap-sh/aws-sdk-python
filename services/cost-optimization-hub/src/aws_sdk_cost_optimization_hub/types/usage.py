"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Usage``."""

from typing_extensions import NotRequired, TypedDict


class Usage(TypedDict, closed=True):
    usage_type: NotRequired["str"]
    """<p>The usage type.</p>"""
    usage_amount: NotRequired["float"]
    """<p>The usage amount.</p>"""
    operation: NotRequired["str"]
    """<p>The operation value.</p>"""
    product_code: NotRequired["str"]
    """<p>The product code.</p>"""
    unit: NotRequired["str"]
    """<p>The usage unit.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Usage) -> dict:
    out: dict = {}
    if "usage_type" in value:
        out["usageType"] = value["usage_type"]
    if "usage_amount" in value:
        out["usageAmount"] = value["usage_amount"]
    if "operation" in value:
        out["operation"] = value["operation"]
    if "product_code" in value:
        out["productCode"] = value["product_code"]
    if "unit" in value:
        out["unit"] = value["unit"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Usage:
    out: Usage = {}  # type: ignore[typeddict-item]
    if "usageType" in data:
        out["usage_type"] = data["usageType"]
    if "usageAmount" in data:
        out["usage_amount"] = data["usageAmount"]
    if "operation" in data:
        out["operation"] = data["operation"]
    if "productCode" in data:
        out["product_code"] = data["productCode"]
    if "unit" in data:
        out["unit"] = data["unit"]
    return out
