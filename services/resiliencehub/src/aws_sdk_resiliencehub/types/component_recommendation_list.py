"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ComponentRecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.component_recommendation

ComponentRecommendationList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.component_recommendation.ComponentRecommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentRecommendationList) -> list:
    import aws_sdk_resiliencehub.types.component_recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehub.types.component_recommendation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ComponentRecommendationList:
    import aws_sdk_resiliencehub.types.component_recommendation

    out: ComponentRecommendationList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehub.types.component_recommendation.deserialize_json(item)
        )
    return out
