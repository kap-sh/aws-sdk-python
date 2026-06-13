"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#UsageBasedRateCardList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.usage_based_rate_card_item

UsageBasedRateCardList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.usage_based_rate_card_item.UsageBasedRateCardItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageBasedRateCardList) -> list:
    import aws_sdk_marketplace_discovery.types.usage_based_rate_card_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.usage_based_rate_card_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> UsageBasedRateCardList:
    import aws_sdk_marketplace_discovery.types.usage_based_rate_card_item

    out: UsageBasedRateCardList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.usage_based_rate_card_item.deserialize_json(
                item
            )
        )
    return out
