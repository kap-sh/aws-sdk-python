"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PricingModelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.pricing_model

PricingModelList: TypeAlias = list[
    "capo_marketplace_discovery.types.pricing_model.PricingModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: PricingModelList) -> list:
    import capo_marketplace_discovery.types.pricing_model

    out: list = []
    for item in value:
        out.append(capo_marketplace_discovery.types.pricing_model.serialize_json(item))
    return out


def deserialize_json(data: list) -> PricingModelList:
    import capo_marketplace_discovery.types.pricing_model

    out: PricingModelList = []
    for item in data:
        out.append(
            capo_marketplace_discovery.types.pricing_model.deserialize_json(item)
        )
    return out
