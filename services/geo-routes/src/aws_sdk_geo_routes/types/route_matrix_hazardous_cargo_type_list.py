"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixHazardousCargoTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_matrix_hazardous_cargo_type

RouteMatrixHazardousCargoTypeList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_matrix_hazardous_cargo_type.RouteMatrixHazardousCargoType"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixHazardousCargoTypeList) -> list:
    import aws_sdk_geo_routes.types.route_matrix_hazardous_cargo_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_matrix_hazardous_cargo_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RouteMatrixHazardousCargoTypeList:
    import aws_sdk_geo_routes.types.route_matrix_hazardous_cargo_type

    out: RouteMatrixHazardousCargoTypeList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_matrix_hazardous_cargo_type.deserialize_json(
                item
            )
        )
    return out
