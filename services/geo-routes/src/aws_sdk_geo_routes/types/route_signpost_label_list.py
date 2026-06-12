"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSignpostLabelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_signpost_label

RouteSignpostLabelList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_signpost_label.RouteSignpostLabel"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSignpostLabelList) -> list:
    import aws_sdk_geo_routes.types.route_signpost_label

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_signpost_label.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteSignpostLabelList:
    import aws_sdk_geo_routes.types.route_signpost_label

    out: RouteSignpostLabelList = []
    for item in data:
        out.append(aws_sdk_geo_routes.types.route_signpost_label.deserialize_json(item))
    return out
