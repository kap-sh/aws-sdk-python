"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RecommendationTemplateStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.recommendation_template_status

RecommendationTemplateStatusList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.recommendation_template_status.RecommendationTemplateStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationTemplateStatusList) -> list:
    import aws_sdk_resiliencehub.types.recommendation_template_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehub.types.recommendation_template_status.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecommendationTemplateStatusList:
    import aws_sdk_resiliencehub.types.recommendation_template_status

    out: RecommendationTemplateStatusList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehub.types.recommendation_template_status.deserialize_json(
                item
            )
        )
    return out
