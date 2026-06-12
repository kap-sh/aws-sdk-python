"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteIntermodalEnabledLegsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_intermodal_enabled_legs

RouteIntermodalEnabledLegsList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_intermodal_enabled_legs.RouteIntermodalEnabledLegs"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteIntermodalEnabledLegsList) -> list:
    import aws_sdk_geo_routes.types.route_intermodal_enabled_legs

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_intermodal_enabled_legs.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteIntermodalEnabledLegsList:
    import aws_sdk_geo_routes.types.route_intermodal_enabled_legs

    out: RouteIntermodalEnabledLegsList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_intermodal_enabled_legs.deserialize_json(
                item
            )
        )
    return out
