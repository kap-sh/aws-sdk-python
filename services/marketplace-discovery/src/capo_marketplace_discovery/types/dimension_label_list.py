"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#DimensionLabelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.dimension_label

DimensionLabelList: TypeAlias = list[
    "capo_marketplace_discovery.types.dimension_label.DimensionLabel"
]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionLabelList) -> list:
    import capo_marketplace_discovery.types.dimension_label

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_discovery.types.dimension_label.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DimensionLabelList:
    import capo_marketplace_discovery.types.dimension_label

    out: DimensionLabelList = []
    for item in data:
        out.append(
            capo_marketplace_discovery.types.dimension_label.deserialize_json(item)
        )
    return out
