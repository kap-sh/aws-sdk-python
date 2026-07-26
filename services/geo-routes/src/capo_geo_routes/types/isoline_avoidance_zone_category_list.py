"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineAvoidanceZoneCategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.isoline_avoidance_zone_category

IsolineAvoidanceZoneCategoryList: TypeAlias = list[
    "capo_geo_routes.types.isoline_avoidance_zone_category.IsolineAvoidanceZoneCategory"
]


# --- restJson1 ser/de ---
def serialize_json(value: IsolineAvoidanceZoneCategoryList) -> list:
    import capo_geo_routes.types.isoline_avoidance_zone_category

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.isoline_avoidance_zone_category.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IsolineAvoidanceZoneCategoryList:
    import capo_geo_routes.types.isoline_avoidance_zone_category

    out: IsolineAvoidanceZoneCategoryList = []
    for item in data:
        out.append(
            capo_geo_routes.types.isoline_avoidance_zone_category.deserialize_json(item)
        )
    return out
