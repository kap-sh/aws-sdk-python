"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialHeatmapConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_heatmap_color_scale


class GeospatialHeatmapConfiguration(TypedDict, closed=True):
    heatmap_color: NotRequired[
        "capo_quicksight.types.geospatial_heatmap_color_scale.GeospatialHeatmapColorScale"
    ]
    """<p>The color scale specification for the heatmap point style.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialHeatmapConfiguration) -> dict:
    out: dict = {}
    if "heatmap_color" in value:
        import capo_quicksight.types.geospatial_heatmap_color_scale

        out["HeatmapColor"] = (
            capo_quicksight.types.geospatial_heatmap_color_scale.serialize_json(
                value["heatmap_color"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialHeatmapConfiguration:
    out: GeospatialHeatmapConfiguration = {}  # type: ignore[typeddict-item]
    if "HeatmapColor" in data:
        import capo_quicksight.types.geospatial_heatmap_color_scale

        out["heatmap_color"] = (
            capo_quicksight.types.geospatial_heatmap_color_scale.deserialize_json(
                data["HeatmapColor"]
            )
        )
    return out
