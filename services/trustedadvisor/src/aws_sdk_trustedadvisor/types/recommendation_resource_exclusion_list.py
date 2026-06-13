"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationResourceExclusionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_trustedadvisor.types.recommendation_resource_exclusion

RecommendationResourceExclusionList: TypeAlias = list[
    "aws_sdk_trustedadvisor.types.recommendation_resource_exclusion.RecommendationResourceExclusion"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationResourceExclusionList) -> list:
    import aws_sdk_trustedadvisor.types.recommendation_resource_exclusion

    out: list = []
    for item in value:
        out.append(
            aws_sdk_trustedadvisor.types.recommendation_resource_exclusion.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecommendationResourceExclusionList:
    import aws_sdk_trustedadvisor.types.recommendation_resource_exclusion

    out: RecommendationResourceExclusionList = []
    for item in data:
        out.append(
            aws_sdk_trustedadvisor.types.recommendation_resource_exclusion.deserialize_json(
                item
            )
        )
    return out
