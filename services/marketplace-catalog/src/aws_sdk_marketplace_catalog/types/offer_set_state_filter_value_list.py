"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSetStateFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.offer_set_state_string

OfferSetStateFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.offer_set_state_string.OfferSetStateString"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferSetStateFilterValueList) -> list:
    import aws_sdk_marketplace_catalog.types.offer_set_state_string

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_catalog.types.offer_set_state_string.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OfferSetStateFilterValueList:
    import aws_sdk_marketplace_catalog.types.offer_set_state_string

    out: OfferSetStateFilterValueList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_catalog.types.offer_set_state_string.deserialize_json(
                item
            )
        )
    return out
