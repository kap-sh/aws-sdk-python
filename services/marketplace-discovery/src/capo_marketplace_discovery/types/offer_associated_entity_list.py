"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#OfferAssociatedEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.offer_associated_entity

OfferAssociatedEntityList: TypeAlias = list[
    "capo_marketplace_discovery.types.offer_associated_entity.OfferAssociatedEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferAssociatedEntityList) -> list:
    import capo_marketplace_discovery.types.offer_associated_entity

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_discovery.types.offer_associated_entity.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OfferAssociatedEntityList:
    import capo_marketplace_discovery.types.offer_associated_entity

    out: OfferAssociatedEntityList = []
    for item in data:
        out.append(
            capo_marketplace_discovery.types.offer_associated_entity.deserialize_json(
                item
            )
        )
    return out
