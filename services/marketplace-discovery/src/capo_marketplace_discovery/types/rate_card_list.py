"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#RateCardList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.rate_card_item

RateCardList: TypeAlias = list[
    "capo_marketplace_discovery.types.rate_card_item.RateCardItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: RateCardList) -> list:
    import capo_marketplace_discovery.types.rate_card_item

    out: list = []
    for item in value:
        out.append(capo_marketplace_discovery.types.rate_card_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> RateCardList:
    import capo_marketplace_discovery.types.rate_card_item

    out: RateCardList = []
    for item in data:
        out.append(
            capo_marketplace_discovery.types.rate_card_item.deserialize_json(item)
        )
    return out
