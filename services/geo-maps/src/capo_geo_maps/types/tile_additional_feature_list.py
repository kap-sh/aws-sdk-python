"""Generated from Smithy shape ``com.amazonaws.geomaps#TileAdditionalFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_maps.types.tile_additional_feature

TileAdditionalFeatureList: TypeAlias = list[
    "capo_geo_maps.types.tile_additional_feature.TileAdditionalFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: TileAdditionalFeatureList) -> list:
    return list(value)


def deserialize_json(data: list) -> TileAdditionalFeatureList:
    return list(data)
