"""Generated from Smithy shape ``com.amazonaws.drs#ProductCode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.product_code_id
    import capo_drs.types.product_code_mode


class ProductCode(TypedDict, closed=True):
    product_code_id: NotRequired["capo_drs.types.product_code_id.ProductCodeId"]
    """<p>Id of a product code associated with a volume.</p>"""
    product_code_mode: NotRequired["capo_drs.types.product_code_mode.ProductCodeMode"]
    """<p>Mode of a product code associated with a volume.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProductCode) -> dict:
    out: dict = {}
    if "product_code_id" in value:
        out["productCodeId"] = value["product_code_id"]
    if "product_code_mode" in value:
        out["productCodeMode"] = value["product_code_mode"]
    return out


def deserialize_json(data: dict) -> ProductCode:
    out: ProductCode = {}  # type: ignore[typeddict-item]
    if "productCodeId" in data:
        out["product_code_id"] = data["productCodeId"]
    if "productCodeMode" in data:
        out["product_code_mode"] = data["productCodeMode"]
    return out
