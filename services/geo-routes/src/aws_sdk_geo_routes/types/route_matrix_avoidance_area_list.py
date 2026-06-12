"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixAvoidanceAreaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_matrix_avoidance_area

RouteMatrixAvoidanceAreaList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_matrix_avoidance_area.RouteMatrixAvoidanceArea"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixAvoidanceAreaList) -> list:
    import aws_sdk_geo_routes.types.route_matrix_avoidance_area

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_matrix_avoidance_area.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteMatrixAvoidanceAreaList:
    import aws_sdk_geo_routes.types.route_matrix_avoidance_area

    out: RouteMatrixAvoidanceAreaList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_matrix_avoidance_area.deserialize_json(item)
        )
    return out
