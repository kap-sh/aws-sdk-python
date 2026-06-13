"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListingSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.listing_summary

ListingSummaryList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.listing_summary.ListingSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListingSummaryList) -> list:
    import aws_sdk_marketplace_discovery.types.listing_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.listing_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListingSummaryList:
    import aws_sdk_marketplace_discovery.types.listing_summary

    out: ListingSummaryList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.listing_summary.deserialize_json(item)
        )
    return out
