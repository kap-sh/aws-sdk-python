"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSignpostLabelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_signpost_label

RouteSignpostLabelList: TypeAlias = list[
    "capo_geo_routes.types.route_signpost_label.RouteSignpostLabel"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSignpostLabelList) -> list:
    import capo_geo_routes.types.route_signpost_label

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_signpost_label.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteSignpostLabelList:
    import capo_geo_routes.types.route_signpost_label

    out: RouteSignpostLabelList = []
    for item in data:
        out.append(capo_geo_routes.types.route_signpost_label.deserialize_json(item))
    return out
