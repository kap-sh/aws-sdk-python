"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#UpdatePurchaseOrdersInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.purchase_orders


class UpdatePurchaseOrdersInput(TypedDict):
    purchase_orders: (
        "aws_sdk_marketplace_agreement.types.purchase_orders.PurchaseOrders"
    )
    """<p>Contains information about purchase order associations.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePurchaseOrdersInput) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_agreement.types.purchase_orders

    out["purchaseOrders"] = (
        aws_sdk_marketplace_agreement.types.purchase_orders.serialize_aws_json_1_0(
            value["purchase_orders"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdatePurchaseOrdersInput:
    out: UpdatePurchaseOrdersInput = {}  # type: ignore[typeddict-item]
    if "purchaseOrders" in data:
        import aws_sdk_marketplace_agreement.types.purchase_orders

        out["purchase_orders"] = (
            aws_sdk_marketplace_agreement.types.purchase_orders.deserialize_aws_json_1_0(
                data["purchaseOrders"]
            )
        )
    else:
        raise DeserializationError("UpdatePurchaseOrdersInput.purchase_orders required")
    return out
