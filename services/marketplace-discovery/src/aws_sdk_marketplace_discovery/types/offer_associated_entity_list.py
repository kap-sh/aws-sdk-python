"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#OfferAssociatedEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.offer_associated_entity

OfferAssociatedEntityList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.offer_associated_entity.OfferAssociatedEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferAssociatedEntityList) -> list:
    import aws_sdk_marketplace_discovery.types.offer_associated_entity

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.offer_associated_entity.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OfferAssociatedEntityList:
    import aws_sdk_marketplace_discovery.types.offer_associated_entity

    out: OfferAssociatedEntityList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.offer_associated_entity.deserialize_json(
                item
            )
        )
    return out
