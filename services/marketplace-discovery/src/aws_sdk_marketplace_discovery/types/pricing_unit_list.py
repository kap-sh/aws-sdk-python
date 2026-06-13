"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PricingUnitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.pricing_unit

PricingUnitList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.pricing_unit.PricingUnit"
]


# --- restJson1 ser/de ---
def serialize_json(value: PricingUnitList) -> list:
    import aws_sdk_marketplace_discovery.types.pricing_unit

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.pricing_unit.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PricingUnitList:
    import aws_sdk_marketplace_discovery.types.pricing_unit

    out: PricingUnitList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.pricing_unit.deserialize_json(item)
        )
    return out
