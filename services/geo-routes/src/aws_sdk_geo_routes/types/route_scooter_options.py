"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteScooterOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_engine_type
    import aws_sdk_geo_routes.types.route_vehicle_license_plate
    import aws_sdk_geo_routes.types.sensitive_integer
    import aws_sdk_geo_routes.types.speed_kilometers_per_hour


class RouteScooterOptions(TypedDict, closed=True):
    engine_type: NotRequired[
        "aws_sdk_geo_routes.types.route_engine_type.RouteEngineType"
    ]
    r"""<p> Engine type of the vehicle. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    license_plate: NotRequired[
        "aws_sdk_geo_routes.types.route_vehicle_license_plate.RouteVehicleLicensePlate"
    ]
    """<p>The vehicle License Plate.</p>"""
    max_speed: NotRequired[
        "aws_sdk_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    ]
    r"""<p> Maximum speed Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""
    occupancy: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    r"""<p> The number of occupants in the vehicle. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p> <p>Default value: <code>1</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteScooterOptions) -> dict:
    out: dict = {}
    if "engine_type" in value:
        import aws_sdk_geo_routes.types.route_engine_type

        out["EngineType"] = aws_sdk_geo_routes.types.route_engine_type.serialize_json(
            value["engine_type"]
        )
    if "license_plate" in value:
        import aws_sdk_geo_routes.types.route_vehicle_license_plate

        out["LicensePlate"] = (
            aws_sdk_geo_routes.types.route_vehicle_license_plate.serialize_json(
                value["license_plate"]
            )
        )
    if "max_speed" in value:
        out["MaxSpeed"] = value["max_speed"]
    if "occupancy" in value:
        out["Occupancy"] = value["occupancy"]
    return out


def deserialize_json(data: dict) -> RouteScooterOptions:
    out: RouteScooterOptions = {}  # type: ignore[typeddict-item]
    if "EngineType" in data:
        import aws_sdk_geo_routes.types.route_engine_type

        out["engine_type"] = (
            aws_sdk_geo_routes.types.route_engine_type.deserialize_json(
                data["EngineType"]
            )
        )
    if "LicensePlate" in data:
        import aws_sdk_geo_routes.types.route_vehicle_license_plate

        out["license_plate"] = (
            aws_sdk_geo_routes.types.route_vehicle_license_plate.deserialize_json(
                data["LicensePlate"]
            )
        )
    if "MaxSpeed" in data:
        out["max_speed"] = data["MaxSpeed"]
    if "Occupancy" in data:
        out["occupancy"] = data["Occupancy"]
    return out
