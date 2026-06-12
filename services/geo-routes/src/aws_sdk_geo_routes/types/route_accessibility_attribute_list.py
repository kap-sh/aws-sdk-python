"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAccessibilityAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_accessibility_attribute

RouteAccessibilityAttributeList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_accessibility_attribute.RouteAccessibilityAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteAccessibilityAttributeList) -> list:
    import aws_sdk_geo_routes.types.route_accessibility_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_accessibility_attribute.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteAccessibilityAttributeList:
    import aws_sdk_geo_routes.types.route_accessibility_attribute

    out: RouteAccessibilityAttributeList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_accessibility_attribute.deserialize_json(
                item
            )
        )
    return out
