"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixDestinationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_matrix_destination

RouteMatrixDestinationList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_matrix_destination.RouteMatrixDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixDestinationList) -> list:
    import aws_sdk_geo_routes.types.route_matrix_destination

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_matrix_destination.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteMatrixDestinationList:
    import aws_sdk_geo_routes.types.route_matrix_destination

    out: RouteMatrixDestinationList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_matrix_destination.deserialize_json(item)
        )
    return out
