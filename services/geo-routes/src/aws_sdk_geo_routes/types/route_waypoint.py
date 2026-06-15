"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteWaypoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.distance_meters
    import aws_sdk_geo_routes.types.duration_seconds
    import aws_sdk_geo_routes.types.heading
    import aws_sdk_geo_routes.types.position
    import aws_sdk_geo_routes.types.route_matching_options
    import aws_sdk_geo_routes.types.route_side_of_street_options
    import aws_sdk_geo_routes.types.sensitive_boolean


class RouteWaypoint(TypedDict):
    avoid_actions_for_distance: (
        "aws_sdk_geo_routes.types.distance_meters.DistanceMeters"
    )
    r"""<p> Avoids actions for the provided distance. This is typically to consider for users in moving vehicles who may not have sufficient time to make an action at an origin or a destination. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    avoid_u_turns: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    r"""<p> Avoid U-turns for calculation on highways and motorways. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    heading: "aws_sdk_geo_routes.types.heading.Heading"
    r"""<p> GPS Heading at the position. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    matching: NotRequired[
        "aws_sdk_geo_routes.types.route_matching_options.RouteMatchingOptions"
    ]
    r"""<p> Options to configure matching the provided position to the road network. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    pass_through: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    r"""<p> If the waypoint should not be treated as a stop. If yes, the waypoint is passed through and doesn't split the route into different legs. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    position: "aws_sdk_geo_routes.types.position.Position"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    side_of_street: NotRequired[
        "aws_sdk_geo_routes.types.route_side_of_street_options.RouteSideOfStreetOptions"
    ]
    r"""<p> Options to configure matching the provided position to a side of the street. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    stop_duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    r"""<p> Duration of the stop. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p> <p> <b>Unit</b>: <code>seconds</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteWaypoint) -> dict:
    out: dict = {}
    out["AvoidActionsForDistance"] = value.get("avoid_actions_for_distance", 0)
    if "avoid_u_turns" in value:
        out["AvoidUTurns"] = value["avoid_u_turns"]
    out["Heading"] = value.get("heading", 0)
    if "matching" in value:
        import aws_sdk_geo_routes.types.route_matching_options

        out["Matching"] = (
            aws_sdk_geo_routes.types.route_matching_options.serialize_json(
                value["matching"]
            )
        )
    if "pass_through" in value:
        out["PassThrough"] = value["pass_through"]
    import aws_sdk_geo_routes.types.position

    out["Position"] = aws_sdk_geo_routes.types.position.serialize_json(
        value["position"]
    )
    if "side_of_street" in value:
        import aws_sdk_geo_routes.types.route_side_of_street_options

        out["SideOfStreet"] = (
            aws_sdk_geo_routes.types.route_side_of_street_options.serialize_json(
                value["side_of_street"]
            )
        )
    out["StopDuration"] = value.get("stop_duration", 0)
    return out


def deserialize_json(data: dict) -> RouteWaypoint:
    out: RouteWaypoint = {}  # type: ignore[typeddict-item]
    if "AvoidActionsForDistance" in data:
        out["avoid_actions_for_distance"] = data["AvoidActionsForDistance"]
    else:
        out["avoid_actions_for_distance"] = 0
    if "AvoidUTurns" in data:
        out["avoid_u_turns"] = data["AvoidUTurns"]
    if "Heading" in data:
        out["heading"] = data["Heading"]
    else:
        out["heading"] = 0
    if "Matching" in data:
        import aws_sdk_geo_routes.types.route_matching_options

        out["matching"] = (
            aws_sdk_geo_routes.types.route_matching_options.deserialize_json(
                data["Matching"]
            )
        )
    if "PassThrough" in data:
        out["pass_through"] = data["PassThrough"]
    if "Position" in data:
        import aws_sdk_geo_routes.types.position

        out["position"] = aws_sdk_geo_routes.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("RouteWaypoint.position required")
    if "SideOfStreet" in data:
        import aws_sdk_geo_routes.types.route_side_of_street_options

        out["side_of_street"] = (
            aws_sdk_geo_routes.types.route_side_of_street_options.deserialize_json(
                data["SideOfStreet"]
            )
        )
    if "StopDuration" in data:
        out["stop_duration"] = data["StopDuration"]
    else:
        out["stop_duration"] = 0
    return out
