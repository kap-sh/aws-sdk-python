"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineDestinationOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.distance_meters
    import aws_sdk_geo_routes.types.heading
    import aws_sdk_geo_routes.types.isoline_matching_options
    import aws_sdk_geo_routes.types.isoline_side_of_street_options


class IsolineDestinationOptions(TypedDict):
    avoid_actions_for_distance: (
        "aws_sdk_geo_routes.types.distance_meters.DistanceMeters"
    )
    """<p>The distance in meters from the destination point within which certain routing actions (such as U-turns or left turns across traffic) are restricted. This helps generate more practical routes by avoiding potentially dangerous maneuvers near the endpoint.</p>"""
    heading: "aws_sdk_geo_routes.types.heading.Heading"
    """<p>The initial direction of travel in degrees (0-360, where 0 is north). This can affect which road segments are considered accessible from the starting point.</p>"""
    matching: NotRequired[
        "aws_sdk_geo_routes.types.isoline_matching_options.IsolineMatchingOptions"
    ]
    """<p>Controls how the destination point is matched to the road network, including search radius and name-based matching preferences.</p>"""
    side_of_street: NotRequired[
        "aws_sdk_geo_routes.types.isoline_side_of_street_options.IsolineSideOfStreetOptions"
    ]
    """<p>Specifies which side of the street should be considered accessible, which is important when building entrances or parking access points are only reachable from one side of the road.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineDestinationOptions) -> dict:
    out: dict = {}
    out["AvoidActionsForDistance"] = value.get("avoid_actions_for_distance", 0)
    out["Heading"] = value.get("heading", 0)
    if "matching" in value:
        import aws_sdk_geo_routes.types.isoline_matching_options

        out["Matching"] = (
            aws_sdk_geo_routes.types.isoline_matching_options.serialize_json(
                value["matching"]
            )
        )
    if "side_of_street" in value:
        import aws_sdk_geo_routes.types.isoline_side_of_street_options

        out["SideOfStreet"] = (
            aws_sdk_geo_routes.types.isoline_side_of_street_options.serialize_json(
                value["side_of_street"]
            )
        )
    return out


def deserialize_json(data: dict) -> IsolineDestinationOptions:
    out: IsolineDestinationOptions = {}  # type: ignore[typeddict-item]
    if "AvoidActionsForDistance" in data:
        out["avoid_actions_for_distance"] = data["AvoidActionsForDistance"]
    else:
        out["avoid_actions_for_distance"] = 0
    if "Heading" in data:
        out["heading"] = data["Heading"]
    else:
        out["heading"] = 0
    if "Matching" in data:
        import aws_sdk_geo_routes.types.isoline_matching_options

        out["matching"] = (
            aws_sdk_geo_routes.types.isoline_matching_options.deserialize_json(
                data["Matching"]
            )
        )
    if "SideOfStreet" in data:
        import aws_sdk_geo_routes.types.isoline_side_of_street_options

        out["side_of_street"] = (
            aws_sdk_geo_routes.types.isoline_side_of_street_options.deserialize_json(
                data["SideOfStreet"]
            )
        )
    return out
