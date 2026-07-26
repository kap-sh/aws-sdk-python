"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialMapState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_coordinate_bounds
    import capo_quicksight.types.geospatial_map_navigation


class GeospatialMapState(TypedDict, closed=True):
    bounds: NotRequired[
        "capo_quicksight.types.geospatial_coordinate_bounds.GeospatialCoordinateBounds"
    ]
    map_navigation: NotRequired[
        "capo_quicksight.types.geospatial_map_navigation.GeospatialMapNavigation"
    ]
    """<p>Enables or disables map navigation for a map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialMapState) -> dict:
    out: dict = {}
    if "bounds" in value:
        import capo_quicksight.types.geospatial_coordinate_bounds

        out["Bounds"] = (
            capo_quicksight.types.geospatial_coordinate_bounds.serialize_json(
                value["bounds"]
            )
        )
    if "map_navigation" in value:
        import capo_quicksight.types.geospatial_map_navigation

        out["MapNavigation"] = (
            capo_quicksight.types.geospatial_map_navigation.serialize_json(
                value["map_navigation"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialMapState:
    out: GeospatialMapState = {}  # type: ignore[typeddict-item]
    if "Bounds" in data:
        import capo_quicksight.types.geospatial_coordinate_bounds

        out["bounds"] = (
            capo_quicksight.types.geospatial_coordinate_bounds.deserialize_json(
                data["Bounds"]
            )
        )
    if "MapNavigation" in data:
        import capo_quicksight.types.geospatial_map_navigation

        out["map_navigation"] = (
            capo_quicksight.types.geospatial_map_navigation.deserialize_json(
                data["MapNavigation"]
            )
        )
    return out
