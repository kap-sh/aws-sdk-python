"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RecommendationTemplateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.recommendation_template

RecommendationTemplateList: TypeAlias = list[
    "capo_resiliencehub.types.recommendation_template.RecommendationTemplate"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationTemplateList) -> list:
    import capo_resiliencehub.types.recommendation_template

    out: list = []
    for item in value:
        out.append(
            capo_resiliencehub.types.recommendation_template.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RecommendationTemplateList:
    import capo_resiliencehub.types.recommendation_template

    out: RecommendationTemplateList = []
    for item in data:
        out.append(
            capo_resiliencehub.types.recommendation_template.deserialize_json(item)
        )
    return out
