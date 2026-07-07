"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteDestinationOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.distance_meters
    import aws_sdk_geo_routes.types.duration_seconds
    import aws_sdk_geo_routes.types.heading
    import aws_sdk_geo_routes.types.route_matching_options
    import aws_sdk_geo_routes.types.route_side_of_street_options
    import aws_sdk_geo_routes.types.sensitive_boolean


class RouteDestinationOptions(TypedDict, closed=True):
    avoid_actions_for_distance: (
        "aws_sdk_geo_routes.types.distance_meters.DistanceMeters"
    )
    """<p>The distance in meters from the destination point within which certain routing actions (such as U-turns or left turns across traffic) are restricted. This helps generate more practical routes by avoiding potentially dangerous maneuvers near the endpoint.</p>"""
    avoid_u_turns: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Avoid U-turns for calculation on highways and motorways.</p>"""
    heading: "aws_sdk_geo_routes.types.heading.Heading"
    """<p>GPS Heading at the position.</p>"""
    matching: NotRequired[
        "aws_sdk_geo_routes.types.route_matching_options.RouteMatchingOptions"
    ]
    """<p>Options to configure matching the provided position to the road network.</p>"""
    side_of_street: NotRequired[
        "aws_sdk_geo_routes.types.route_side_of_street_options.RouteSideOfStreetOptions"
    ]
    """<p>Options to configure matching the provided position to a side of the street.</p>"""
    stop_duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the stop.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteDestinationOptions) -> dict:
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
    if "side_of_street" in value:
        import aws_sdk_geo_routes.types.route_side_of_street_options

        out["SideOfStreet"] = (
            aws_sdk_geo_routes.types.route_side_of_street_options.serialize_json(
                value["side_of_street"]
            )
        )
    out["StopDuration"] = value.get("stop_duration", 0)
    return out


def deserialize_json(data: dict) -> RouteDestinationOptions:
    out: RouteDestinationOptions = {}  # type: ignore[typeddict-item]
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
