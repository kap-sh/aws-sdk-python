"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#InfrastructureAndCodeRecommendationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.infrastructure_and_code_recommendation

InfrastructureAndCodeRecommendationsList: TypeAlias = list[
    "capo_resiliencehubv2.types.infrastructure_and_code_recommendation.InfrastructureAndCodeRecommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: InfrastructureAndCodeRecommendationsList) -> list:
    import capo_resiliencehubv2.types.infrastructure_and_code_recommendation

    out: list = []
    for item in value:
        out.append(
            capo_resiliencehubv2.types.infrastructure_and_code_recommendation.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InfrastructureAndCodeRecommendationsList:
    import capo_resiliencehubv2.types.infrastructure_and_code_recommendation

    out: InfrastructureAndCodeRecommendationsList = []
    for item in data:
        out.append(
            capo_resiliencehubv2.types.infrastructure_and_code_recommendation.deserialize_json(
                item
            )
        )
    return out
