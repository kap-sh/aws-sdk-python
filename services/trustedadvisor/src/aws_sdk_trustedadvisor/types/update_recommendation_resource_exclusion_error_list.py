"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#UpdateRecommendationResourceExclusionErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_trustedadvisor.types.update_recommendation_resource_exclusion_error

UpdateRecommendationResourceExclusionErrorList: TypeAlias = list[
    "aws_sdk_trustedadvisor.types.update_recommendation_resource_exclusion_error.UpdateRecommendationResourceExclusionError"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommendationResourceExclusionErrorList) -> list:
    import aws_sdk_trustedadvisor.types.update_recommendation_resource_exclusion_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_trustedadvisor.types.update_recommendation_resource_exclusion_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> UpdateRecommendationResourceExclusionErrorList:
    import aws_sdk_trustedadvisor.types.update_recommendation_resource_exclusion_error

    out: UpdateRecommendationResourceExclusionErrorList = []
    for item in data:
        out.append(
            aws_sdk_trustedadvisor.types.update_recommendation_resource_exclusion_error.deserialize_json(
                item
            )
        )
    return out
