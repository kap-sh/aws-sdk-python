"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialPointStyleOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.cluster_marker_configuration
    import capo_quicksight.types.geospatial_heatmap_configuration
    import capo_quicksight.types.geospatial_selected_point_style


class GeospatialPointStyleOptions(TypedDict, closed=True):
    selected_point_style: NotRequired[
        "capo_quicksight.types.geospatial_selected_point_style.GeospatialSelectedPointStyle"
    ]
    """<p>The selected point styles (point, cluster) of the geospatial map.</p>"""
    cluster_marker_configuration: NotRequired[
        "capo_quicksight.types.cluster_marker_configuration.ClusterMarkerConfiguration"
    ]
    """<p>The cluster marker configuration of the geospatial point style.</p>"""
    heatmap_configuration: NotRequired[
        "capo_quicksight.types.geospatial_heatmap_configuration.GeospatialHeatmapConfiguration"
    ]
    """<p>The heatmap configuration of the geospatial point style.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialPointStyleOptions) -> dict:
    out: dict = {}
    if "selected_point_style" in value:
        import capo_quicksight.types.geospatial_selected_point_style

        out["SelectedPointStyle"] = (
            capo_quicksight.types.geospatial_selected_point_style.serialize_json(
                value["selected_point_style"]
            )
        )
    if "cluster_marker_configuration" in value:
        import capo_quicksight.types.cluster_marker_configuration

        out["ClusterMarkerConfiguration"] = (
            capo_quicksight.types.cluster_marker_configuration.serialize_json(
                value["cluster_marker_configuration"]
            )
        )
    if "heatmap_configuration" in value:
        import capo_quicksight.types.geospatial_heatmap_configuration

        out["HeatmapConfiguration"] = (
            capo_quicksight.types.geospatial_heatmap_configuration.serialize_json(
                value["heatmap_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialPointStyleOptions:
    out: GeospatialPointStyleOptions = {}  # type: ignore[typeddict-item]
    if "SelectedPointStyle" in data:
        import capo_quicksight.types.geospatial_selected_point_style

        out["selected_point_style"] = (
            capo_quicksight.types.geospatial_selected_point_style.deserialize_json(
                data["SelectedPointStyle"]
            )
        )
    if "ClusterMarkerConfiguration" in data:
        import capo_quicksight.types.cluster_marker_configuration

        out["cluster_marker_configuration"] = (
            capo_quicksight.types.cluster_marker_configuration.deserialize_json(
                data["ClusterMarkerConfiguration"]
            )
        )
    if "HeatmapConfiguration" in data:
        import capo_quicksight.types.geospatial_heatmap_configuration

        out["heatmap_configuration"] = (
            capo_quicksight.types.geospatial_heatmap_configuration.deserialize_json(
                data["HeatmapConfiguration"]
            )
        )
    return out
