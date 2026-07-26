"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialWindowOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_coordinate_bounds
    import capo_quicksight.types.map_zoom_mode


class GeospatialWindowOptions(TypedDict, closed=True):
    bounds: NotRequired[
        "capo_quicksight.types.geospatial_coordinate_bounds.GeospatialCoordinateBounds"
    ]
    """<p>The bounds options (north, south, west, east) of the geospatial window options.</p>"""
    map_zoom_mode: NotRequired["capo_quicksight.types.map_zoom_mode.MapZoomMode"]
    """<p>The map zoom modes (manual, auto) of the geospatial window options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialWindowOptions) -> dict:
    out: dict = {}
    if "bounds" in value:
        import capo_quicksight.types.geospatial_coordinate_bounds

        out["Bounds"] = (
            capo_quicksight.types.geospatial_coordinate_bounds.serialize_json(
                value["bounds"]
            )
        )
    if "map_zoom_mode" in value:
        import capo_quicksight.types.map_zoom_mode

        out["MapZoomMode"] = capo_quicksight.types.map_zoom_mode.serialize_json(
            value["map_zoom_mode"]
        )
    return out


def deserialize_json(data: dict) -> GeospatialWindowOptions:
    out: GeospatialWindowOptions = {}  # type: ignore[typeddict-item]
    if "Bounds" in data:
        import capo_quicksight.types.geospatial_coordinate_bounds

        out["bounds"] = (
            capo_quicksight.types.geospatial_coordinate_bounds.deserialize_json(
                data["Bounds"]
            )
        )
    if "MapZoomMode" in data:
        import capo_quicksight.types.map_zoom_mode

        out["map_zoom_mode"] = capo_quicksight.types.map_zoom_mode.deserialize_json(
            data["MapZoomMode"]
        )
    return out
