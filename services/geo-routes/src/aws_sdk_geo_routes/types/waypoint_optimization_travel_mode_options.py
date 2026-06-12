"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationTravelModeOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.waypoint_optimization_pedestrian_options
    import aws_sdk_geo_routes.types.waypoint_optimization_truck_options


class WaypointOptimizationTravelModeOptions(TypedDict):
    pedestrian: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_pedestrian_options.WaypointOptimizationPedestrianOptions"
    ]
    """<p>Travel mode options when the provided travel mode is <code>Pedestrian</code>.</p>"""
    truck: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_truck_options.WaypointOptimizationTruckOptions"
    ]
    """<p>Travel mode options when the provided travel mode is <code>Truck</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationTravelModeOptions) -> dict:
    out: dict = {}
    if "pedestrian" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_pedestrian_options

        out["Pedestrian"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_pedestrian_options.serialize_json(
                value["pedestrian"]
            )
        )
    if "truck" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_truck_options

        out["Truck"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_truck_options.serialize_json(
                value["truck"]
            )
        )
    return out


def deserialize_json(data: dict) -> WaypointOptimizationTravelModeOptions:
    out: WaypointOptimizationTravelModeOptions = {}  # type: ignore[typeddict-item]
    if "Pedestrian" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_pedestrian_options

        out["pedestrian"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_pedestrian_options.deserialize_json(
                data["Pedestrian"]
            )
        )
    if "Truck" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_truck_options

        out["truck"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_truck_options.deserialize_json(
                data["Truck"]
            )
        )
    return out
