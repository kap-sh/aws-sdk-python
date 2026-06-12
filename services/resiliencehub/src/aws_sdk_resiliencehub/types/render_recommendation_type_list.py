"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RenderRecommendationTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.render_recommendation_type

RenderRecommendationTypeList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.render_recommendation_type.RenderRecommendationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: RenderRecommendationTypeList) -> list:
    import aws_sdk_resiliencehub.types.render_recommendation_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehub.types.render_recommendation_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RenderRecommendationTypeList:
    import aws_sdk_resiliencehub.types.render_recommendation_type

    out: RenderRecommendationTypeList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehub.types.render_recommendation_type.deserialize_json(
                item
            )
        )
    return out
