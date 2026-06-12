"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixAvoidanceZoneCategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_matrix_avoidance_zone_category

RouteMatrixAvoidanceZoneCategoryList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_matrix_avoidance_zone_category.RouteMatrixAvoidanceZoneCategory"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixAvoidanceZoneCategoryList) -> list:
    import aws_sdk_geo_routes.types.route_matrix_avoidance_zone_category

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_matrix_avoidance_zone_category.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RouteMatrixAvoidanceZoneCategoryList:
    import aws_sdk_geo_routes.types.route_matrix_avoidance_zone_category

    out: RouteMatrixAvoidanceZoneCategoryList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_matrix_avoidance_zone_category.deserialize_json(
                item
            )
        )
    return out
