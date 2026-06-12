"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMajorRoadLabelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_major_road_label

RouteMajorRoadLabelList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_major_road_label.RouteMajorRoadLabel"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteMajorRoadLabelList) -> list:
    import aws_sdk_geo_routes.types.route_major_road_label

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_major_road_label.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteMajorRoadLabelList:
    import aws_sdk_geo_routes.types.route_major_road_label

    out: RouteMajorRoadLabelList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_major_road_label.deserialize_json(item)
        )
    return out
