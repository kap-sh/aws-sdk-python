"""Generated from Smithy shape ``com.amazonaws.georoutes#OptimizeWaypointsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.api_key
    import aws_sdk_geo_routes.types.position
    import aws_sdk_geo_routes.types.timestamp_with_timezone_offset
    import aws_sdk_geo_routes.types.waypoint_optimization_avoidance_options
    import aws_sdk_geo_routes.types.waypoint_optimization_clustering_options
    import aws_sdk_geo_routes.types.waypoint_optimization_destination_options
    import aws_sdk_geo_routes.types.waypoint_optimization_driver_options
    import aws_sdk_geo_routes.types.waypoint_optimization_exclusion_options
    import aws_sdk_geo_routes.types.waypoint_optimization_origin_options
    import aws_sdk_geo_routes.types.waypoint_optimization_sequencing_objective
    import aws_sdk_geo_routes.types.waypoint_optimization_traffic_options
    import aws_sdk_geo_routes.types.waypoint_optimization_travel_mode
    import aws_sdk_geo_routes.types.waypoint_optimization_travel_mode_options
    import aws_sdk_geo_routes.types.waypoint_optimization_waypoint_list


class OptimizeWaypointsRequest(TypedDict):
    avoid: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_avoidance_options.WaypointOptimizationAvoidanceOptions"
    ]
    """<p>Features that are avoided. Avoidance is on a best-case basis. If an avoidance can't be satisfied for a particular case, this setting is ignored.</p>"""
    clustering: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_clustering_options.WaypointOptimizationClusteringOptions"
    ]
    """<p>Clustering allows you to specify how nearby waypoints can be clustered to improve the optimized sequence.</p>"""
    departure_time: NotRequired[
        "aws_sdk_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>Departure time from the waypoint.</p> <p>Time format:<code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>"""
    destination: NotRequired["aws_sdk_geo_routes.types.position.Position"]
    """<p>The final position for the route in the World Geodetic System (WGS 84) format: <code>[longitude, latitude]</code>.</p>"""
    destination_options: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_destination_options.WaypointOptimizationDestinationOptions"
    ]
    """<p>Destination related options.</p>"""
    driver: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_driver_options.WaypointOptimizationDriverOptions"
    ]
    """<p>Driver related options.</p>"""
    exclude: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_exclusion_options.WaypointOptimizationExclusionOptions"
    ]
    """<p>Features to be strictly excluded while calculating the route.</p>"""
    key: NotRequired["aws_sdk_geo_routes.types.api_key.ApiKey"]
    """<p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request. </p>"""
    optimize_sequencing_for: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_sequencing_objective.WaypointOptimizationSequencingObjective"
    ]
    """<p>Specifies the optimization criteria for the calculated sequence.</p> <p>Default value: <code>FastestRoute</code>.</p>"""
    origin: "aws_sdk_geo_routes.types.position.Position"
    """<p>The start position for the route in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    origin_options: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_origin_options.WaypointOptimizationOriginOptions"
    ]
    """<p>Origin related options.</p>"""
    traffic: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_traffic_options.WaypointOptimizationTrafficOptions"
    ]
    """<p>Traffic-related options.</p>"""
    travel_mode: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_travel_mode.WaypointOptimizationTravelMode"
    ]
    """<p>Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility.</p> <p>Default value: <code>Car</code> </p>"""
    travel_mode_options: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_travel_mode_options.WaypointOptimizationTravelModeOptions"
    ]
    """<p>Travel mode related options for the provided travel mode.</p>"""
    waypoints: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_waypoint_list.WaypointOptimizationWaypointList"
    ]
    """<p>List of waypoints between the <code>Origin</code> and <code>Destination</code>, in World Geodetic System (WGS 84) format: [longitude, latitude].</p> <p>The maximum number of waypoints allowed per request:</p> <ul> <li> <p>Maximum 50 waypoints per request</p> </li> <li> <p>Maximum 20 waypoints when using constraints (<code>AccessHours</code>, <code>AppointmentTime</code>, <code>ServiceDuration</code>, <code>Heading</code>, <code>SideOfStreet</code>, <code>Before</code>)</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: OptimizeWaypointsRequest) -> dict:
    out: dict = {}
    if "avoid" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_avoidance_options

        out["Avoid"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_avoidance_options.serialize_json(
                value["avoid"]
            )
        )
    if "clustering" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_clustering_options

        out["Clustering"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_clustering_options.serialize_json(
                value["clustering"]
            )
        )
    if "departure_time" in value:
        out["DepartureTime"] = value["departure_time"]
    if "destination" in value:
        import aws_sdk_geo_routes.types.position

        out["Destination"] = aws_sdk_geo_routes.types.position.serialize_json(
            value["destination"]
        )
    if "destination_options" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_destination_options

        out["DestinationOptions"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_destination_options.serialize_json(
                value["destination_options"]
            )
        )
    if "driver" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_driver_options

        out["Driver"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_driver_options.serialize_json(
                value["driver"]
            )
        )
    if "exclude" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_exclusion_options

        out["Exclude"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_exclusion_options.serialize_json(
                value["exclude"]
            )
        )
    if "optimize_sequencing_for" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_sequencing_objective

        out["OptimizeSequencingFor"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_sequencing_objective.serialize_json(
                value["optimize_sequencing_for"]
            )
        )
    import aws_sdk_geo_routes.types.position

    out["Origin"] = aws_sdk_geo_routes.types.position.serialize_json(value["origin"])
    if "origin_options" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_origin_options

        out["OriginOptions"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_origin_options.serialize_json(
                value["origin_options"]
            )
        )
    if "traffic" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_traffic_options

        out["Traffic"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_traffic_options.serialize_json(
                value["traffic"]
            )
        )
    if "travel_mode" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_travel_mode

        out["TravelMode"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_travel_mode.serialize_json(
                value["travel_mode"]
            )
        )
    if "travel_mode_options" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_travel_mode_options

        out["TravelModeOptions"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_travel_mode_options.serialize_json(
                value["travel_mode_options"]
            )
        )
    if "waypoints" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_waypoint_list

        out["Waypoints"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_waypoint_list.serialize_json(
                value["waypoints"]
            )
        )
    return out


def deserialize_json(data: dict) -> OptimizeWaypointsRequest:
    out: OptimizeWaypointsRequest = {}  # type: ignore[typeddict-item]
    if "Avoid" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_avoidance_options

        out["avoid"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_avoidance_options.deserialize_json(
                data["Avoid"]
            )
        )
    if "Clustering" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_clustering_options

        out["clustering"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_clustering_options.deserialize_json(
                data["Clustering"]
            )
        )
    if "DepartureTime" in data:
        out["departure_time"] = data["DepartureTime"]
    if "Destination" in data:
        import aws_sdk_geo_routes.types.position

        out["destination"] = aws_sdk_geo_routes.types.position.deserialize_json(
            data["Destination"]
        )
    if "DestinationOptions" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_destination_options

        out["destination_options"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_destination_options.deserialize_json(
                data["DestinationOptions"]
            )
        )
    if "Driver" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_driver_options

        out["driver"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_driver_options.deserialize_json(
                data["Driver"]
            )
        )
    if "Exclude" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_exclusion_options

        out["exclude"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_exclusion_options.deserialize_json(
                data["Exclude"]
            )
        )
    if "OptimizeSequencingFor" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_sequencing_objective

        out["optimize_sequencing_for"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_sequencing_objective.deserialize_json(
                data["OptimizeSequencingFor"]
            )
        )
    if "Origin" in data:
        import aws_sdk_geo_routes.types.position

        out["origin"] = aws_sdk_geo_routes.types.position.deserialize_json(
            data["Origin"]
        )
    else:
        raise DeserializationError("OptimizeWaypointsRequest.origin required")
    if "OriginOptions" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_origin_options

        out["origin_options"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_origin_options.deserialize_json(
                data["OriginOptions"]
            )
        )
    if "Traffic" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_traffic_options

        out["traffic"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_traffic_options.deserialize_json(
                data["Traffic"]
            )
        )
    if "TravelMode" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_travel_mode

        out["travel_mode"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_travel_mode.deserialize_json(
                data["TravelMode"]
            )
        )
    if "TravelModeOptions" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_travel_mode_options

        out["travel_mode_options"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_travel_mode_options.deserialize_json(
                data["TravelModeOptions"]
            )
        )
    if "Waypoints" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_waypoint_list

        out["waypoints"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_waypoint_list.deserialize_json(
                data["Waypoints"]
            )
        )
    return out
