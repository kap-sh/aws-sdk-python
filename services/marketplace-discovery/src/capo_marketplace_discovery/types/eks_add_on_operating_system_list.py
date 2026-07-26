"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#EksAddOnOperatingSystemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.eks_add_on_operating_system

EksAddOnOperatingSystemList: TypeAlias = list[
    "capo_marketplace_discovery.types.eks_add_on_operating_system.EksAddOnOperatingSystem"
]


# --- restJson1 ser/de ---
def serialize_json(value: EksAddOnOperatingSystemList) -> list:
    import capo_marketplace_discovery.types.eks_add_on_operating_system

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_discovery.types.eks_add_on_operating_system.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EksAddOnOperatingSystemList:
    import capo_marketplace_discovery.types.eks_add_on_operating_system

    out: EksAddOnOperatingSystemList = []
    for item in data:
        out.append(
            capo_marketplace_discovery.types.eks_add_on_operating_system.deserialize_json(
                item
            )
        )
    return out
