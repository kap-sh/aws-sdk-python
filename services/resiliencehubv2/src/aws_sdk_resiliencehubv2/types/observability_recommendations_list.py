"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ObservabilityRecommendationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.observability_recommendation

ObservabilityRecommendationsList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.observability_recommendation.ObservabilityRecommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ObservabilityRecommendationsList) -> list:
    import aws_sdk_resiliencehubv2.types.observability_recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehubv2.types.observability_recommendation.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ObservabilityRecommendationsList:
    import aws_sdk_resiliencehubv2.types.observability_recommendation

    out: ObservabilityRecommendationsList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehubv2.types.observability_recommendation.deserialize_json(
                item
            )
        )
    return out
