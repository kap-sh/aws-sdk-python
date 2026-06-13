"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.purchase_option_summary

PurchaseOptionSummaryList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.purchase_option_summary.PurchaseOptionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOptionSummaryList) -> list:
    import aws_sdk_marketplace_discovery.types.purchase_option_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.purchase_option_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PurchaseOptionSummaryList:
    import aws_sdk_marketplace_discovery.types.purchase_option_summary

    out: PurchaseOptionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.purchase_option_summary.deserialize_json(
                item
            )
        )
    return out
