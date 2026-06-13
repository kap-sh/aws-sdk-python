"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#OfferSetAssociatedEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.offer_set_associated_entity

OfferSetAssociatedEntityList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.offer_set_associated_entity.OfferSetAssociatedEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferSetAssociatedEntityList) -> list:
    import aws_sdk_marketplace_discovery.types.offer_set_associated_entity

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.offer_set_associated_entity.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OfferSetAssociatedEntityList:
    import aws_sdk_marketplace_discovery.types.offer_set_associated_entity

    out: OfferSetAssociatedEntityList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.offer_set_associated_entity.deserialize_json(
                item
            )
        )
    return out
