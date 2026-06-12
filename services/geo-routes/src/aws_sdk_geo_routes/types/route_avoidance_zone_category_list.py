"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAvoidanceZoneCategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_avoidance_zone_category

RouteAvoidanceZoneCategoryList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_avoidance_zone_category.RouteAvoidanceZoneCategory"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteAvoidanceZoneCategoryList) -> list:
    import aws_sdk_geo_routes.types.route_avoidance_zone_category

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_avoidance_zone_category.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteAvoidanceZoneCategoryList:
    import aws_sdk_geo_routes.types.route_avoidance_zone_category

    out: RouteAvoidanceZoneCategoryList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_avoidance_zone_category.deserialize_json(
                item
            )
        )
    return out
