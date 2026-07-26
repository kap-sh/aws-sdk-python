"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PricingUnitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.pricing_unit

PricingUnitList: TypeAlias = list[
    "capo_marketplace_discovery.types.pricing_unit.PricingUnit"
]


# --- restJson1 ser/de ---
def serialize_json(value: PricingUnitList) -> list:
    import capo_marketplace_discovery.types.pricing_unit

    out: list = []
    for item in value:
        out.append(capo_marketplace_discovery.types.pricing_unit.serialize_json(item))
    return out


def deserialize_json(data: list) -> PricingUnitList:
    import capo_marketplace_discovery.types.pricing_unit

    out: PricingUnitList = []
    for item in data:
        out.append(capo_marketplace_discovery.types.pricing_unit.deserialize_json(item))
    return out
