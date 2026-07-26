"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteLegAdditionalFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_leg_additional_feature

RouteLegAdditionalFeatureList: TypeAlias = list[
    "capo_geo_routes.types.route_leg_additional_feature.RouteLegAdditionalFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteLegAdditionalFeatureList) -> list:
    import capo_geo_routes.types.route_leg_additional_feature

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_leg_additional_feature.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteLegAdditionalFeatureList:
    import capo_geo_routes.types.route_leg_additional_feature

    out: RouteLegAdditionalFeatureList = []
    for item in data:
        out.append(
            capo_geo_routes.types.route_leg_additional_feature.deserialize_json(item)
        )
    return out
