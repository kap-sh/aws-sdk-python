"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ConfigurableUpfrontRateCardList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.configurable_upfront_rate_card_item

ConfigurableUpfrontRateCardList: TypeAlias = list[
    "capo_marketplace_discovery.types.configurable_upfront_rate_card_item.ConfigurableUpfrontRateCardItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurableUpfrontRateCardList) -> list:
    import capo_marketplace_discovery.types.configurable_upfront_rate_card_item

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_discovery.types.configurable_upfront_rate_card_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfigurableUpfrontRateCardList:
    import capo_marketplace_discovery.types.configurable_upfront_rate_card_item

    out: ConfigurableUpfrontRateCardList = []
    for item in data:
        out.append(
            capo_marketplace_discovery.types.configurable_upfront_rate_card_item.deserialize_json(
                item
            )
        )
    return out
