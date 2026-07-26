"""Generated from Smithy shape ``com.amazonaws.geoplaces#QueryRefinementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.query_refinement

QueryRefinementList: TypeAlias = list[
    "capo_geo_places.types.query_refinement.QueryRefinement"
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryRefinementList) -> list:
    import capo_geo_places.types.query_refinement

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.query_refinement.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueryRefinementList:
    import capo_geo_places.types.query_refinement

    out: QueryRefinementList = []
    for item in data:
        out.append(capo_geo_places.types.query_refinement.deserialize_json(item))
    return out
