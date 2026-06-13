"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialHeatmapColorScale``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_heatmap_data_color_list


class GeospatialHeatmapColorScale(TypedDict):
    colors: NotRequired[
        "aws_sdk_quicksight.types.geospatial_heatmap_data_color_list.GeospatialHeatmapDataColorList"
    ]
    """<p>The list of colors to be used in heatmap point style.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialHeatmapColorScale) -> dict:
    out: dict = {}
    if "colors" in value:
        import aws_sdk_quicksight.types.geospatial_heatmap_data_color_list

        out["Colors"] = (
            aws_sdk_quicksight.types.geospatial_heatmap_data_color_list.serialize_json(
                value["colors"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialHeatmapColorScale:
    out: GeospatialHeatmapColorScale = {}  # type: ignore[typeddict-item]
    if "Colors" in data:
        import aws_sdk_quicksight.types.geospatial_heatmap_data_color_list

        out["colors"] = (
            aws_sdk_quicksight.types.geospatial_heatmap_data_color_list.deserialize_json(
                data["Colors"]
            )
        )
    return out
