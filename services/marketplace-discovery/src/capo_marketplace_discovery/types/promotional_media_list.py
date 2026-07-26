"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PromotionalMediaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.promotional_media

PromotionalMediaList: TypeAlias = list[
    "capo_marketplace_discovery.types.promotional_media.PromotionalMedia"
]


# --- restJson1 ser/de ---
def serialize_json(value: PromotionalMediaList) -> list:
    import capo_marketplace_discovery.types.promotional_media

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_discovery.types.promotional_media.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PromotionalMediaList:
    import capo_marketplace_discovery.types.promotional_media

    out: PromotionalMediaList = []
    for item in data:
        out.append(
            capo_marketplace_discovery.types.promotional_media.deserialize_json(item)
        )
    return out
