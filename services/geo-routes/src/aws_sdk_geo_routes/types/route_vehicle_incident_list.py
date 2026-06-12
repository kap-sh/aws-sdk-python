"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleIncidentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_vehicle_incident

RouteVehicleIncidentList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_vehicle_incident.RouteVehicleIncident"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleIncidentList) -> list:
    import aws_sdk_geo_routes.types.route_vehicle_incident

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_vehicle_incident.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteVehicleIncidentList:
    import aws_sdk_geo_routes.types.route_vehicle_incident

    out: RouteVehicleIncidentList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_vehicle_incident.deserialize_json(item)
        )
    return out
