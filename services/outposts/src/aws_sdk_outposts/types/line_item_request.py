"""Generated from Smithy shape ``com.amazonaws.outposts#LineItemRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.line_item_quantity
    import aws_sdk_outposts.types.sku_code


class LineItemRequest(TypedDict, closed=True):
    catalog_item_id: NotRequired["aws_sdk_outposts.types.sku_code.SkuCode"]
    """<p>The ID of the catalog item.</p>"""
    quantity: NotRequired["aws_sdk_outposts.types.line_item_quantity.LineItemQuantity"]
    """<p>The quantity of a line item request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineItemRequest) -> dict:
    out: dict = {}
    if "catalog_item_id" in value:
        out["CatalogItemId"] = value["catalog_item_id"]
    if "quantity" in value:
        out["Quantity"] = value["quantity"]
    return out


def deserialize_json(data: dict) -> LineItemRequest:
    out: LineItemRequest = {}  # type: ignore[typeddict-item]
    if "CatalogItemId" in data:
        out["catalog_item_id"] = data["CatalogItemId"]
    if "Quantity" in data:
        out["quantity"] = data["Quantity"]
    return out
