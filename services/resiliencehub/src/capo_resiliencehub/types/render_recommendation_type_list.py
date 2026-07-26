"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RenderRecommendationTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.render_recommendation_type

RenderRecommendationTypeList: TypeAlias = list[
    "capo_resiliencehub.types.render_recommendation_type.RenderRecommendationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: RenderRecommendationTypeList) -> list:
    import capo_resiliencehub.types.render_recommendation_type

    out: list = []
    for item in value:
        out.append(
            capo_resiliencehub.types.render_recommendation_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RenderRecommendationTypeList:
    import capo_resiliencehub.types.render_recommendation_type

    out: RenderRecommendationTypeList = []
    for item in data:
        out.append(
            capo_resiliencehub.types.render_recommendation_type.deserialize_json(item)
        )
    return out
