"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMajorRoadLabel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.localized_string
    import aws_sdk_geo_routes.types.route_number


class RouteMajorRoadLabel(TypedDict, closed=True):
    road_name: NotRequired["aws_sdk_geo_routes.types.localized_string.LocalizedString"]
    """<p>Name of the road (localized).</p>"""
    route_number: NotRequired["aws_sdk_geo_routes.types.route_number.RouteNumber"]
    """<p>Route number of the road.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMajorRoadLabel) -> dict:
    out: dict = {}
    if "road_name" in value:
        import aws_sdk_geo_routes.types.localized_string

        out["RoadName"] = aws_sdk_geo_routes.types.localized_string.serialize_json(
            value["road_name"]
        )
    if "route_number" in value:
        import aws_sdk_geo_routes.types.route_number

        out["RouteNumber"] = aws_sdk_geo_routes.types.route_number.serialize_json(
            value["route_number"]
        )
    return out


def deserialize_json(data: dict) -> RouteMajorRoadLabel:
    out: RouteMajorRoadLabel = {}  # type: ignore[typeddict-item]
    if "RoadName" in data:
        import aws_sdk_geo_routes.types.localized_string

        out["road_name"] = aws_sdk_geo_routes.types.localized_string.deserialize_json(
            data["RoadName"]
        )
    if "RouteNumber" in data:
        import aws_sdk_geo_routes.types.route_number

        out["route_number"] = aws_sdk_geo_routes.types.route_number.deserialize_json(
            data["RouteNumber"]
        )
    return out
