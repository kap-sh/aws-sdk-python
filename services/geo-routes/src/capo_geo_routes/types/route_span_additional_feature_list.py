"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanAdditionalFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_span_additional_feature

RouteSpanAdditionalFeatureList: TypeAlias = list[
    "capo_geo_routes.types.route_span_additional_feature.RouteSpanAdditionalFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanAdditionalFeatureList) -> list:
    import capo_geo_routes.types.route_span_additional_feature

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_span_additional_feature.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteSpanAdditionalFeatureList:
    import capo_geo_routes.types.route_span_additional_feature

    out: RouteSpanAdditionalFeatureList = []
    for item in data:
        out.append(
            capo_geo_routes.types.route_span_additional_feature.deserialize_json(item)
        )
    return out
