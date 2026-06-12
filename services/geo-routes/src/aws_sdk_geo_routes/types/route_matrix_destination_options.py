"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixDestinationOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.distance_meters
    import aws_sdk_geo_routes.types.heading
    import aws_sdk_geo_routes.types.route_matrix_matching_options
    import aws_sdk_geo_routes.types.route_matrix_side_of_street_options


class RouteMatrixDestinationOptions(TypedDict):
    avoid_actions_for_distance: (
        "aws_sdk_geo_routes.types.distance_meters.DistanceMeters"
    )
    """<p>Avoids actions for the provided distance. This is typically to consider for users in moving vehicles who may not have sufficient time to make an action at an origin or a destination.</p>"""
    heading: "aws_sdk_geo_routes.types.heading.Heading"
    """<p>GPS Heading at the position.</p>"""
    matching: NotRequired[
        "aws_sdk_geo_routes.types.route_matrix_matching_options.RouteMatrixMatchingOptions"
    ]
    """<p>Options to configure matching the provided position to the road network.</p>"""
    side_of_street: NotRequired[
        "aws_sdk_geo_routes.types.route_matrix_side_of_street_options.RouteMatrixSideOfStreetOptions"
    ]
    """<p>Options to configure matching the provided position to a side of the street.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixDestinationOptions) -> dict:
    out: dict = {}
    out["AvoidActionsForDistance"] = value.get("avoid_actions_for_distance", 0)
    out["Heading"] = value.get("heading", 0)
    if "matching" in value:
        import aws_sdk_geo_routes.types.route_matrix_matching_options

        out["Matching"] = (
            aws_sdk_geo_routes.types.route_matrix_matching_options.serialize_json(
                value["matching"]
            )
        )
    if "side_of_street" in value:
        import aws_sdk_geo_routes.types.route_matrix_side_of_street_options

        out["SideOfStreet"] = (
            aws_sdk_geo_routes.types.route_matrix_side_of_street_options.serialize_json(
                value["side_of_street"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteMatrixDestinationOptions:
    out: RouteMatrixDestinationOptions = {}  # type: ignore[typeddict-item]
    if "AvoidActionsForDistance" in data:
        out["avoid_actions_for_distance"] = data["AvoidActionsForDistance"]
    else:
        out["avoid_actions_for_distance"] = 0
    if "Heading" in data:
        out["heading"] = data["Heading"]
    else:
        out["heading"] = 0
    if "Matching" in data:
        import aws_sdk_geo_routes.types.route_matrix_matching_options

        out["matching"] = (
            aws_sdk_geo_routes.types.route_matrix_matching_options.deserialize_json(
                data["Matching"]
            )
        )
    if "SideOfStreet" in data:
        import aws_sdk_geo_routes.types.route_matrix_side_of_street_options

        out["side_of_street"] = (
            aws_sdk_geo_routes.types.route_matrix_side_of_street_options.deserialize_json(
                data["SideOfStreet"]
            )
        )
    return out
