"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiPlace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.position23
    import aws_sdk_geo_routes.types.route_access_point_details
    import aws_sdk_geo_routes.types.route_station_details
    import aws_sdk_geo_routes.types.route_taxi_place_type
    import aws_sdk_geo_routes.types.sensitive_integer
    import aws_sdk_geo_routes.types.sensitive_string


class RouteTaxiPlace(TypedDict, closed=True):
    access_point_details: NotRequired[
        "aws_sdk_geo_routes.types.route_access_point_details.RouteAccessPointDetails"
    ]
    """<p>Details of the access point.</p>"""
    name: NotRequired["aws_sdk_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>The name of the place.</p>"""
    original_position: NotRequired["aws_sdk_geo_routes.types.position23.Position23"]
    """<p>Position provided in the request.</p>"""
    position: "aws_sdk_geo_routes.types.position23.Position23"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    station_details: NotRequired[
        "aws_sdk_geo_routes.types.route_station_details.RouteStationDetails"
    ]
    """<p>Details about the station.</p>"""
    type: NotRequired[
        "aws_sdk_geo_routes.types.route_taxi_place_type.RouteTaxiPlaceType"
    ]
    """<p>The type of the place.</p>"""
    waypoint_index: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>Index of the waypoint in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiPlace) -> dict:
    out: dict = {}
    if "access_point_details" in value:
        import aws_sdk_geo_routes.types.route_access_point_details

        out["AccessPointDetails"] = (
            aws_sdk_geo_routes.types.route_access_point_details.serialize_json(
                value["access_point_details"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "original_position" in value:
        import aws_sdk_geo_routes.types.position23

        out["OriginalPosition"] = aws_sdk_geo_routes.types.position23.serialize_json(
            value["original_position"]
        )
    import aws_sdk_geo_routes.types.position23

    out["Position"] = aws_sdk_geo_routes.types.position23.serialize_json(
        value["position"]
    )
    if "station_details" in value:
        import aws_sdk_geo_routes.types.route_station_details

        out["StationDetails"] = (
            aws_sdk_geo_routes.types.route_station_details.serialize_json(
                value["station_details"]
            )
        )
    if "type" in value:
        import aws_sdk_geo_routes.types.route_taxi_place_type

        out["Type"] = aws_sdk_geo_routes.types.route_taxi_place_type.serialize_json(
            value["type"]
        )
    if "waypoint_index" in value:
        out["WaypointIndex"] = value["waypoint_index"]
    return out


def deserialize_json(data: dict) -> RouteTaxiPlace:
    out: RouteTaxiPlace = {}  # type: ignore[typeddict-item]
    if "AccessPointDetails" in data:
        import aws_sdk_geo_routes.types.route_access_point_details

        out["access_point_details"] = (
            aws_sdk_geo_routes.types.route_access_point_details.deserialize_json(
                data["AccessPointDetails"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "OriginalPosition" in data:
        import aws_sdk_geo_routes.types.position23

        out["original_position"] = aws_sdk_geo_routes.types.position23.deserialize_json(
            data["OriginalPosition"]
        )
    if "Position" in data:
        import aws_sdk_geo_routes.types.position23

        out["position"] = aws_sdk_geo_routes.types.position23.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("RouteTaxiPlace.position required")
    if "StationDetails" in data:
        import aws_sdk_geo_routes.types.route_station_details

        out["station_details"] = (
            aws_sdk_geo_routes.types.route_station_details.deserialize_json(
                data["StationDetails"]
            )
        )
    if "Type" in data:
        import aws_sdk_geo_routes.types.route_taxi_place_type

        out["type"] = aws_sdk_geo_routes.types.route_taxi_place_type.deserialize_json(
            data["Type"]
        )
    if "WaypointIndex" in data:
        out["waypoint_index"] = data["WaypointIndex"]
    return out
