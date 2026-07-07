"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehiclePlace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.position23
    import aws_sdk_geo_routes.types.route_access_point_details
    import aws_sdk_geo_routes.types.route_side_of_street
    import aws_sdk_geo_routes.types.route_station_details
    import aws_sdk_geo_routes.types.route_vehicle_place_type
    import aws_sdk_geo_routes.types.sensitive_integer
    import aws_sdk_geo_routes.types.sensitive_string


class RouteVehiclePlace(TypedDict, closed=True):
    name: NotRequired["aws_sdk_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>The name of the place.</p>"""
    original_position: NotRequired["aws_sdk_geo_routes.types.position23.Position23"]
    """<p>Position provided in the request.</p>"""
    position: "aws_sdk_geo_routes.types.position23.Position23"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    side_of_street: NotRequired[
        "aws_sdk_geo_routes.types.route_side_of_street.RouteSideOfStreet"
    ]
    """<p>Options to configure matching the provided position to a side of the street.</p>"""
    waypoint_index: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>Index of the waypoint in the request.</p>"""
    access_point_details: NotRequired[
        "aws_sdk_geo_routes.types.route_access_point_details.RouteAccessPointDetails"
    ]
    """<p>Details of the access point.</p>"""
    station_details: NotRequired[
        "aws_sdk_geo_routes.types.route_station_details.RouteStationDetails"
    ]
    """<p>Details about the station.</p>"""
    type: NotRequired[
        "aws_sdk_geo_routes.types.route_vehicle_place_type.RouteVehiclePlaceType"
    ]
    """<p>The type of the place.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehiclePlace) -> dict:
    out: dict = {}
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
    if "side_of_street" in value:
        import aws_sdk_geo_routes.types.route_side_of_street

        out["SideOfStreet"] = (
            aws_sdk_geo_routes.types.route_side_of_street.serialize_json(
                value["side_of_street"]
            )
        )
    if "waypoint_index" in value:
        out["WaypointIndex"] = value["waypoint_index"]
    if "access_point_details" in value:
        import aws_sdk_geo_routes.types.route_access_point_details

        out["AccessPointDetails"] = (
            aws_sdk_geo_routes.types.route_access_point_details.serialize_json(
                value["access_point_details"]
            )
        )
    if "station_details" in value:
        import aws_sdk_geo_routes.types.route_station_details

        out["StationDetails"] = (
            aws_sdk_geo_routes.types.route_station_details.serialize_json(
                value["station_details"]
            )
        )
    if "type" in value:
        import aws_sdk_geo_routes.types.route_vehicle_place_type

        out["Type"] = aws_sdk_geo_routes.types.route_vehicle_place_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> RouteVehiclePlace:
    out: RouteVehiclePlace = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("RouteVehiclePlace.position required")
    if "SideOfStreet" in data:
        import aws_sdk_geo_routes.types.route_side_of_street

        out["side_of_street"] = (
            aws_sdk_geo_routes.types.route_side_of_street.deserialize_json(
                data["SideOfStreet"]
            )
        )
    if "WaypointIndex" in data:
        out["waypoint_index"] = data["WaypointIndex"]
    if "AccessPointDetails" in data:
        import aws_sdk_geo_routes.types.route_access_point_details

        out["access_point_details"] = (
            aws_sdk_geo_routes.types.route_access_point_details.deserialize_json(
                data["AccessPointDetails"]
            )
        )
    if "StationDetails" in data:
        import aws_sdk_geo_routes.types.route_station_details

        out["station_details"] = (
            aws_sdk_geo_routes.types.route_station_details.deserialize_json(
                data["StationDetails"]
            )
        )
    if "Type" in data:
        import aws_sdk_geo_routes.types.route_vehicle_place_type

        out["type"] = (
            aws_sdk_geo_routes.types.route_vehicle_place_type.deserialize_json(
                data["Type"]
            )
        )
    return out
