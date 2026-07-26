"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#VolumeRecommendationOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.volume_recommendation_option

VolumeRecommendationOptions: TypeAlias = list[
    "capo_compute_optimizer.types.volume_recommendation_option.VolumeRecommendationOption"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VolumeRecommendationOptions) -> list:
    import capo_compute_optimizer.types.volume_recommendation_option

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.volume_recommendation_option.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> VolumeRecommendationOptions:
    import capo_compute_optimizer.types.volume_recommendation_option

    out: VolumeRecommendationOptions = []
    for item in data:
        out.append(
            capo_compute_optimizer.types.volume_recommendation_option.deserialize_aws_json_1_0(
                item
            )
        )
    return out
