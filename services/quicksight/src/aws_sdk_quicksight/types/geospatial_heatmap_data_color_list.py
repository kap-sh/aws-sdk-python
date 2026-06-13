"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialHeatmapDataColorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_heatmap_data_color

GeospatialHeatmapDataColorList: TypeAlias = list[
    "aws_sdk_quicksight.types.geospatial_heatmap_data_color.GeospatialHeatmapDataColor"
]


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialHeatmapDataColorList) -> list:
    import aws_sdk_quicksight.types.geospatial_heatmap_data_color

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.geospatial_heatmap_data_color.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GeospatialHeatmapDataColorList:
    import aws_sdk_quicksight.types.geospatial_heatmap_data_color

    out: GeospatialHeatmapDataColorList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.geospatial_heatmap_data_color.deserialize_json(
                item
            )
        )
    return out
