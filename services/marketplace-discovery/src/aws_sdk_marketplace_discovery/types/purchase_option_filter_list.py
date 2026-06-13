"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.purchase_option_filter

PurchaseOptionFilterList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.purchase_option_filter.PurchaseOptionFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOptionFilterList) -> list:
    import aws_sdk_marketplace_discovery.types.purchase_option_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.purchase_option_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PurchaseOptionFilterList:
    import aws_sdk_marketplace_discovery.types.purchase_option_filter

    out: PurchaseOptionFilterList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.purchase_option_filter.deserialize_json(
                item
            )
        )
    return out
