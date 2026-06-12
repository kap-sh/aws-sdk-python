"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#VolumeRecommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.volume_recommendation

VolumeRecommendations: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.volume_recommendation.VolumeRecommendation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VolumeRecommendations) -> list:
    import aws_sdk_compute_optimizer.types.volume_recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.volume_recommendation.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> VolumeRecommendations:
    import aws_sdk_compute_optimizer.types.volume_recommendation

    out: VolumeRecommendations = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.volume_recommendation.deserialize_aws_json_1_0(
                item
            )
        )
    return out
