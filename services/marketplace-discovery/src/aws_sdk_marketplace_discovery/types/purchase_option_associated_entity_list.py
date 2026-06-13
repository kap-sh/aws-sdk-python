"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionAssociatedEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.purchase_option_associated_entity

PurchaseOptionAssociatedEntityList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.purchase_option_associated_entity.PurchaseOptionAssociatedEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOptionAssociatedEntityList) -> list:
    import aws_sdk_marketplace_discovery.types.purchase_option_associated_entity

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.purchase_option_associated_entity.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PurchaseOptionAssociatedEntityList:
    import aws_sdk_marketplace_discovery.types.purchase_option_associated_entity

    out: PurchaseOptionAssociatedEntityList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.purchase_option_associated_entity.deserialize_json(
                item
            )
        )
    return out
