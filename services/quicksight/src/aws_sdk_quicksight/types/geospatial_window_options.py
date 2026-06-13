"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialWindowOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_coordinate_bounds
    import aws_sdk_quicksight.types.map_zoom_mode


class GeospatialWindowOptions(TypedDict):
    bounds: NotRequired[
        "aws_sdk_quicksight.types.geospatial_coordinate_bounds.GeospatialCoordinateBounds"
    ]
    """<p>The bounds options (north, south, west, east) of the geospatial window options.</p>"""
    map_zoom_mode: NotRequired["aws_sdk_quicksight.types.map_zoom_mode.MapZoomMode"]
    """<p>The map zoom modes (manual, auto) of the geospatial window options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialWindowOptions) -> dict:
    out: dict = {}
    if "bounds" in value:
        import aws_sdk_quicksight.types.geospatial_coordinate_bounds

        out["Bounds"] = (
            aws_sdk_quicksight.types.geospatial_coordinate_bounds.serialize_json(
                value["bounds"]
            )
        )
    if "map_zoom_mode" in value:
        import aws_sdk_quicksight.types.map_zoom_mode

        out["MapZoomMode"] = aws_sdk_quicksight.types.map_zoom_mode.serialize_json(
            value["map_zoom_mode"]
        )
    return out


def deserialize_json(data: dict) -> GeospatialWindowOptions:
    out: GeospatialWindowOptions = {}  # type: ignore[typeddict-item]
    if "Bounds" in data:
        import aws_sdk_quicksight.types.geospatial_coordinate_bounds

        out["bounds"] = (
            aws_sdk_quicksight.types.geospatial_coordinate_bounds.deserialize_json(
                data["Bounds"]
            )
        )
    if "MapZoomMode" in data:
        import aws_sdk_quicksight.types.map_zoom_mode

        out["map_zoom_mode"] = aws_sdk_quicksight.types.map_zoom_mode.deserialize_json(
            data["MapZoomMode"]
        )
    return out
