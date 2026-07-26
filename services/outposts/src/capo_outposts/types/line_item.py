"""Generated from Smithy shape ``com.amazonaws.outposts#LineItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.line_item_asset_information_list
    import capo_outposts.types.line_item_id
    import capo_outposts.types.line_item_quantity
    import capo_outposts.types.line_item_status
    import capo_outposts.types.order_id
    import capo_outposts.types.shipment_information
    import capo_outposts.types.sku_code


class LineItem(TypedDict, closed=True):
    catalog_item_id: NotRequired["capo_outposts.types.sku_code.SkuCode"]
    """<p> The ID of the catalog item.</p>"""
    line_item_id: NotRequired["capo_outposts.types.line_item_id.LineItemId"]
    """<p>The ID of the line item.</p>"""
    quantity: NotRequired["capo_outposts.types.line_item_quantity.LineItemQuantity"]
    """<p>The quantity of the line item.</p>"""
    status: NotRequired["capo_outposts.types.line_item_status.LineItemStatus"]
    """<p>The status of the line item.</p>"""
    shipment_information: NotRequired[
        "capo_outposts.types.shipment_information.ShipmentInformation"
    ]
    """<p> Information about a line item shipment. </p>"""
    asset_information_list: NotRequired[
        "capo_outposts.types.line_item_asset_information_list.LineItemAssetInformationList"
    ]
    """<p> Information about assets. </p>"""
    previous_line_item_id: NotRequired["capo_outposts.types.line_item_id.LineItemId"]
    """<p>The ID of the previous line item.</p>"""
    previous_order_id: NotRequired["capo_outposts.types.order_id.OrderId"]
    """<p>The ID of the previous order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineItem) -> dict:
    out: dict = {}
    if "catalog_item_id" in value:
        out["CatalogItemId"] = value["catalog_item_id"]
    if "line_item_id" in value:
        out["LineItemId"] = value["line_item_id"]
    if "quantity" in value:
        out["Quantity"] = value["quantity"]
    if "status" in value:
        import capo_outposts.types.line_item_status

        out["Status"] = capo_outposts.types.line_item_status.serialize_json(
            value["status"]
        )
    if "shipment_information" in value:
        import capo_outposts.types.shipment_information

        out["ShipmentInformation"] = (
            capo_outposts.types.shipment_information.serialize_json(
                value["shipment_information"]
            )
        )
    if "asset_information_list" in value:
        import capo_outposts.types.line_item_asset_information_list

        out["AssetInformationList"] = (
            capo_outposts.types.line_item_asset_information_list.serialize_json(
                value["asset_information_list"]
            )
        )
    if "previous_line_item_id" in value:
        out["PreviousLineItemId"] = value["previous_line_item_id"]
    if "previous_order_id" in value:
        out["PreviousOrderId"] = value["previous_order_id"]
    return out


def deserialize_json(data: dict) -> LineItem:
    out: LineItem = {}  # type: ignore[typeddict-item]
    if "CatalogItemId" in data:
        out["catalog_item_id"] = data["CatalogItemId"]
    if "LineItemId" in data:
        out["line_item_id"] = data["LineItemId"]
    if "Quantity" in data:
        out["quantity"] = data["Quantity"]
    if "Status" in data:
        import capo_outposts.types.line_item_status

        out["status"] = capo_outposts.types.line_item_status.deserialize_json(
            data["Status"]
        )
    if "ShipmentInformation" in data:
        import capo_outposts.types.shipment_information

        out["shipment_information"] = (
            capo_outposts.types.shipment_information.deserialize_json(
                data["ShipmentInformation"]
            )
        )
    if "AssetInformationList" in data:
        import capo_outposts.types.line_item_asset_information_list

        out["asset_information_list"] = (
            capo_outposts.types.line_item_asset_information_list.deserialize_json(
                data["AssetInformationList"]
            )
        )
    if "PreviousLineItemId" in data:
        out["previous_line_item_id"] = data["PreviousLineItemId"]
    if "PreviousOrderId" in data:
        out["previous_order_id"] = data["PreviousOrderId"]
    return out
