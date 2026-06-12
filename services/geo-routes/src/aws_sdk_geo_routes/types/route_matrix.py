"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrix``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_matrix_row

RouteMatrix: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_matrix_row.RouteMatrixRow"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrix) -> list:
    import aws_sdk_geo_routes.types.route_matrix_row

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_matrix_row.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteMatrix:
    import aws_sdk_geo_routes.types.route_matrix_row

    out: RouteMatrix = []
    for item in data:
        out.append(aws_sdk_geo_routes.types.route_matrix_row.deserialize_json(item))
    return out
