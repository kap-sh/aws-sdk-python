"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PromotionalMediaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.promotional_media

PromotionalMediaList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.promotional_media.PromotionalMedia"
]


# --- restJson1 ser/de ---
def serialize_json(value: PromotionalMediaList) -> list:
    import aws_sdk_marketplace_discovery.types.promotional_media

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.promotional_media.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PromotionalMediaList:
    import aws_sdk_marketplace_discovery.types.promotional_media

    out: PromotionalMediaList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.promotional_media.deserialize_json(item)
        )
    return out
