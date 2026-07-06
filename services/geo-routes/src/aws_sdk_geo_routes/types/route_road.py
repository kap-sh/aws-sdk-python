"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRoad``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.localized_string_list
    import aws_sdk_geo_routes.types.route_number_list
    import aws_sdk_geo_routes.types.route_road_type


class RouteRoad(TypedDict, closed=True):
    road_name: "aws_sdk_geo_routes.types.localized_string_list.LocalizedStringList"
    """<p>Name of the road (localized).</p>"""
    route_number: "aws_sdk_geo_routes.types.route_number_list.RouteNumberList"
    """<p>Route number of the road.</p>"""
    towards: "aws_sdk_geo_routes.types.localized_string_list.LocalizedStringList"
    """<p>Names of destinations that can be reached when traveling on the road.</p>"""
    type: NotRequired["aws_sdk_geo_routes.types.route_road_type.RouteRoadType"]
    """<p>The type of road.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteRoad) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.localized_string_list

    out["RoadName"] = aws_sdk_geo_routes.types.localized_string_list.serialize_json(
        value["road_name"]
    )
    import aws_sdk_geo_routes.types.route_number_list

    out["RouteNumber"] = aws_sdk_geo_routes.types.route_number_list.serialize_json(
        value["route_number"]
    )
    import aws_sdk_geo_routes.types.localized_string_list

    out["Towards"] = aws_sdk_geo_routes.types.localized_string_list.serialize_json(
        value["towards"]
    )
    if "type" in value:
        import aws_sdk_geo_routes.types.route_road_type

        out["Type"] = aws_sdk_geo_routes.types.route_road_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> RouteRoad:
    out: RouteRoad = {}  # type: ignore[typeddict-item]
    if "RoadName" in data:
        import aws_sdk_geo_routes.types.localized_string_list

        out["road_name"] = (
            aws_sdk_geo_routes.types.localized_string_list.deserialize_json(
                data["RoadName"]
            )
        )
    else:
        raise DeserializationError("RouteRoad.road_name required")
    if "RouteNumber" in data:
        import aws_sdk_geo_routes.types.route_number_list

        out["route_number"] = (
            aws_sdk_geo_routes.types.route_number_list.deserialize_json(
                data["RouteNumber"]
            )
        )
    else:
        raise DeserializationError("RouteRoad.route_number required")
    if "Towards" in data:
        import aws_sdk_geo_routes.types.localized_string_list

        out["towards"] = (
            aws_sdk_geo_routes.types.localized_string_list.deserialize_json(
                data["Towards"]
            )
        )
    else:
        raise DeserializationError("RouteRoad.towards required")
    if "Type" in data:
        import aws_sdk_geo_routes.types.route_road_type

        out["type"] = aws_sdk_geo_routes.types.route_road_type.deserialize_json(
            data["Type"]
        )
    return out
