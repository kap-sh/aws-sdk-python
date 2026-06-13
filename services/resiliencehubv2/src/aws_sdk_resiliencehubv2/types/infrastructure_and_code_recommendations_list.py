"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#InfrastructureAndCodeRecommendationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.infrastructure_and_code_recommendation

InfrastructureAndCodeRecommendationsList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.infrastructure_and_code_recommendation.InfrastructureAndCodeRecommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: InfrastructureAndCodeRecommendationsList) -> list:
    import aws_sdk_resiliencehubv2.types.infrastructure_and_code_recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehubv2.types.infrastructure_and_code_recommendation.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InfrastructureAndCodeRecommendationsList:
    import aws_sdk_resiliencehubv2.types.infrastructure_and_code_recommendation

    out: InfrastructureAndCodeRecommendationsList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehubv2.types.infrastructure_and_code_recommendation.deserialize_json(
                item
            )
        )
    return out
