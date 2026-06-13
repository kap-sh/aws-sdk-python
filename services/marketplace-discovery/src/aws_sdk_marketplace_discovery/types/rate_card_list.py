"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#RateCardList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.rate_card_item

RateCardList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.rate_card_item.RateCardItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: RateCardList) -> list:
    import aws_sdk_marketplace_discovery.types.rate_card_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.rate_card_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RateCardList:
    import aws_sdk_marketplace_discovery.types.rate_card_item

    out: RateCardList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.rate_card_item.deserialize_json(item)
        )
    return out
