"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferTargetingFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.offer_targeting_string

OfferTargetingFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.offer_targeting_string.OfferTargetingString"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferTargetingFilterValueList) -> list:
    import capo_marketplace_catalog.types.offer_targeting_string

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_catalog.types.offer_targeting_string.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> OfferTargetingFilterValueList:
    import capo_marketplace_catalog.types.offer_targeting_string

    out: OfferTargetingFilterValueList = []
    for item in data:
        out.append(
            capo_marketplace_catalog.types.offer_targeting_string.deserialize_json(item)
        )
    return out
