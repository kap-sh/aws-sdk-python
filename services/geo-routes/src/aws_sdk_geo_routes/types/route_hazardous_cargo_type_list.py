"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteHazardousCargoTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_hazardous_cargo_type

RouteHazardousCargoTypeList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_hazardous_cargo_type.RouteHazardousCargoType"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteHazardousCargoTypeList) -> list:
    import aws_sdk_geo_routes.types.route_hazardous_cargo_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_hazardous_cargo_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteHazardousCargoTypeList:
    import aws_sdk_geo_routes.types.route_hazardous_cargo_type

    out: RouteHazardousCargoTypeList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_hazardous_cargo_type.deserialize_json(item)
        )
    return out
