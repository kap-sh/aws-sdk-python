"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationAvoidanceOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.sensitive_boolean
    import capo_geo_routes.types.waypoint_optimization_avoidance_area_list


class WaypointOptimizationAvoidanceOptions(TypedDict, closed=True):
    areas: NotRequired[
        "capo_geo_routes.types.waypoint_optimization_avoidance_area_list.WaypointOptimizationAvoidanceAreaList"
    ]
    """<p>Areas to be avoided.</p>"""
    car_shuttle_trains: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Avoidance options for cars-shuttles-trains.</p>"""
    controlled_access_highways: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Avoid controlled access highways while calculating the route.</p>"""
    dirt_roads: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Avoid dirt roads while calculating the route.</p>"""
    ferries: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Avoidance options for ferries.</p>"""
    toll_roads: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Avoids roads where the specified toll transponders are the only mode of payment.</p>"""
    tunnels: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Avoid tunnels while calculating the route.</p>"""
    u_turns: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Avoid U-turns for calculation on highways and motorways.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationAvoidanceOptions) -> dict:
    out: dict = {}
    if "areas" in value:
        import capo_geo_routes.types.waypoint_optimization_avoidance_area_list

        out["Areas"] = (
            capo_geo_routes.types.waypoint_optimization_avoidance_area_list.serialize_json(
                value["areas"]
            )
        )
    if "car_shuttle_trains" in value:
        out["CarShuttleTrains"] = value["car_shuttle_trains"]
    if "controlled_access_highways" in value:
        out["ControlledAccessHighways"] = value["controlled_access_highways"]
    if "dirt_roads" in value:
        out["DirtRoads"] = value["dirt_roads"]
    if "ferries" in value:
        out["Ferries"] = value["ferries"]
    if "toll_roads" in value:
        out["TollRoads"] = value["toll_roads"]
    if "tunnels" in value:
        out["Tunnels"] = value["tunnels"]
    if "u_turns" in value:
        out["UTurns"] = value["u_turns"]
    return out


def deserialize_json(data: dict) -> WaypointOptimizationAvoidanceOptions:
    out: WaypointOptimizationAvoidanceOptions = {}  # type: ignore[typeddict-item]
    if "Areas" in data:
        import capo_geo_routes.types.waypoint_optimization_avoidance_area_list

        out["areas"] = (
            capo_geo_routes.types.waypoint_optimization_avoidance_area_list.deserialize_json(
                data["Areas"]
            )
        )
    if "CarShuttleTrains" in data:
        out["car_shuttle_trains"] = data["CarShuttleTrains"]
    if "ControlledAccessHighways" in data:
        out["controlled_access_highways"] = data["ControlledAccessHighways"]
    if "DirtRoads" in data:
        out["dirt_roads"] = data["DirtRoads"]
    if "Ferries" in data:
        out["ferries"] = data["Ferries"]
    if "TollRoads" in data:
        out["toll_roads"] = data["TollRoads"]
    if "Tunnels" in data:
        out["tunnels"] = data["Tunnels"]
    if "UTurns" in data:
        out["u_turns"] = data["UTurns"]
    return out
