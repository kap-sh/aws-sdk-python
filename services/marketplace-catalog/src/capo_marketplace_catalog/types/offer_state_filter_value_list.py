"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferStateFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.offer_state_string

OfferStateFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.offer_state_string.OfferStateString"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferStateFilterValueList) -> list:
    import capo_marketplace_catalog.types.offer_state_string

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_catalog.types.offer_state_string.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> OfferStateFilterValueList:
    import capo_marketplace_catalog.types.offer_state_string

    out: OfferStateFilterValueList = []
    for item in data:
        out.append(
            capo_marketplace_catalog.types.offer_state_string.deserialize_json(item)
        )
    return out
