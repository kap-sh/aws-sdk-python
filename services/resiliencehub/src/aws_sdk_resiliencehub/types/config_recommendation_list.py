"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ConfigRecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.config_recommendation

ConfigRecommendationList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.config_recommendation.ConfigRecommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigRecommendationList) -> list:
    import aws_sdk_resiliencehub.types.config_recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehub.types.config_recommendation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConfigRecommendationList:
    import aws_sdk_resiliencehub.types.config_recommendation

    out: ConfigRecommendationList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehub.types.config_recommendation.deserialize_json(item)
        )
    return out
