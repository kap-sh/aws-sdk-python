"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#FulfillmentOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.fulfillment_option

FulfillmentOptionsList: TypeAlias = list[
    "capo_marketplace_discovery.types.fulfillment_option.FulfillmentOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: FulfillmentOptionsList) -> list:
    import capo_marketplace_discovery.types.fulfillment_option

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_discovery.types.fulfillment_option.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FulfillmentOptionsList:
    import capo_marketplace_discovery.types.fulfillment_option

    out: FulfillmentOptionsList = []
    for item in data:
        out.append(
            capo_marketplace_discovery.types.fulfillment_option.deserialize_json(item)
        )
    return out
