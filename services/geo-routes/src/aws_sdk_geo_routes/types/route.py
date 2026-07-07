"""Generated from Smithy shape ``com.amazonaws.georoutes#Route``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_leg_list
    import aws_sdk_geo_routes.types.route_major_road_label_list
    import aws_sdk_geo_routes.types.route_summary


class Route(TypedDict, closed=True):
    legs: "aws_sdk_geo_routes.types.route_leg_list.RouteLegList"
    """<p>A leg is a section of a route from one waypoint to the next. A leg could be of type Vehicle, Pedestrian or Ferry. Legs of different types could occur together within a single route. For example, a car employing the use of a Ferry will contain Vehicle legs corresponding to journey on land, and Ferry legs corresponding to the journey via Ferry.</p>"""
    major_road_labels: (
        "aws_sdk_geo_routes.types.route_major_road_label_list.RouteMajorRoadLabelList"
    )
    """<p>Important labels including names and route numbers that differentiate the current route from the alternatives presented.</p>"""
    summary: NotRequired["aws_sdk_geo_routes.types.route_summary.RouteSummary"]
    """<p>Summarized details of the leg.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Route) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.route_leg_list

    out["Legs"] = aws_sdk_geo_routes.types.route_leg_list.serialize_json(value["legs"])
    import aws_sdk_geo_routes.types.route_major_road_label_list

    out["MajorRoadLabels"] = (
        aws_sdk_geo_routes.types.route_major_road_label_list.serialize_json(
            value["major_road_labels"]
        )
    )
    if "summary" in value:
        import aws_sdk_geo_routes.types.route_summary

        out["Summary"] = aws_sdk_geo_routes.types.route_summary.serialize_json(
            value["summary"]
        )
    return out


def deserialize_json(data: dict) -> Route:
    out: Route = {}  # type: ignore[typeddict-item]
    if "Legs" in data:
        import aws_sdk_geo_routes.types.route_leg_list

        out["legs"] = aws_sdk_geo_routes.types.route_leg_list.deserialize_json(
            data["Legs"]
        )
    else:
        raise DeserializationError("Route.legs required")
    if "MajorRoadLabels" in data:
        import aws_sdk_geo_routes.types.route_major_road_label_list

        out["major_road_labels"] = (
            aws_sdk_geo_routes.types.route_major_road_label_list.deserialize_json(
                data["MajorRoadLabels"]
            )
        )
    else:
        raise DeserializationError("Route.major_road_labels required")
    if "Summary" in data:
        import aws_sdk_geo_routes.types.route_summary

        out["summary"] = aws_sdk_geo_routes.types.route_summary.deserialize_json(
            data["Summary"]
        )
    return out
