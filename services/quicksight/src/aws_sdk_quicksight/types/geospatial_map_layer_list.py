"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialMapLayerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_layer_item

GeospatialMapLayerList: TypeAlias = list[
    "aws_sdk_quicksight.types.geospatial_layer_item.GeospatialLayerItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialMapLayerList) -> list:
    import aws_sdk_quicksight.types.geospatial_layer_item

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.geospatial_layer_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> GeospatialMapLayerList:
    import aws_sdk_quicksight.types.geospatial_layer_item

    out: GeospatialMapLayerList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.geospatial_layer_item.deserialize_json(item)
        )
    return out
