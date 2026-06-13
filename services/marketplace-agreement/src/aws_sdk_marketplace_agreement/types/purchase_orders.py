"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#PurchaseOrders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.purchase_order

PurchaseOrders: TypeAlias = list[
    "aws_sdk_marketplace_agreement.types.purchase_order.PurchaseOrder"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PurchaseOrders) -> list:
    import aws_sdk_marketplace_agreement.types.purchase_order

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_agreement.types.purchase_order.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PurchaseOrders:
    import aws_sdk_marketplace_agreement.types.purchase_order

    out: PurchaseOrders = []
    for item in data:
        out.append(
            aws_sdk_marketplace_agreement.types.purchase_order.deserialize_aws_json_1_0(
                item
            )
        )
    return out
