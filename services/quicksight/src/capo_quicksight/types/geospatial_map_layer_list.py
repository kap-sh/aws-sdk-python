"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialMapLayerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_layer_item

GeospatialMapLayerList: TypeAlias = list[
    "capo_quicksight.types.geospatial_layer_item.GeospatialLayerItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialMapLayerList) -> list:
    import capo_quicksight.types.geospatial_layer_item

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.geospatial_layer_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> GeospatialMapLayerList:
    import capo_quicksight.types.geospatial_layer_item

    out: GeospatialMapLayerList = []
    for item in data:
        out.append(capo_quicksight.types.geospatial_layer_item.deserialize_json(item))
    return out
