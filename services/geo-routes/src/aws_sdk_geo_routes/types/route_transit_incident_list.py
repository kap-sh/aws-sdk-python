"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitIncidentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_transit_incident

RouteTransitIncidentList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_transit_incident.RouteTransitIncident"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitIncidentList) -> list:
    import aws_sdk_geo_routes.types.route_transit_incident

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_transit_incident.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteTransitIncidentList:
    import aws_sdk_geo_routes.types.route_transit_incident

    out: RouteTransitIncidentList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_transit_incident.deserialize_json(item)
        )
    return out
