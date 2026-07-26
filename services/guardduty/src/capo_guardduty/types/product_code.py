"""Generated from Smithy shape ``com.amazonaws.guardduty#ProductCode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class ProductCode(TypedDict, closed=True):
    code: NotRequired["capo_guardduty.types.string.String"]
    """<p>The product code information.</p>"""
    product_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>The product code type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProductCode) -> dict:
    out: dict = {}
    if "code" in value:
        out["productCodeId"] = value["code"]
    if "product_type" in value:
        out["productCodeType"] = value["product_type"]
    return out


def deserialize_json(data: dict) -> ProductCode:
    out: ProductCode = {}  # type: ignore[typeddict-item]
    if "productCodeId" in data:
        out["code"] = data["productCodeId"]
    if "productCodeType" in data:
        out["product_type"] = data["productCodeType"]
    return out
