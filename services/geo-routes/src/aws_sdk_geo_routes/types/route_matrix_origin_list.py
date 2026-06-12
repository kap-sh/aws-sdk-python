"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixOriginList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_matrix_origin

RouteMatrixOriginList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_matrix_origin.RouteMatrixOrigin"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixOriginList) -> list:
    import aws_sdk_geo_routes.types.route_matrix_origin

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_matrix_origin.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteMatrixOriginList:
    import aws_sdk_geo_routes.types.route_matrix_origin

    out: RouteMatrixOriginList = []
    for item in data:
        out.append(aws_sdk_geo_routes.types.route_matrix_origin.deserialize_json(item))
    return out
