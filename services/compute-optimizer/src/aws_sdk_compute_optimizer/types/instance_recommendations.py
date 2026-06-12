"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InstanceRecommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.instance_recommendation

InstanceRecommendations: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.instance_recommendation.InstanceRecommendation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceRecommendations) -> list:
    import aws_sdk_compute_optimizer.types.instance_recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.instance_recommendation.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InstanceRecommendations:
    import aws_sdk_compute_optimizer.types.instance_recommendation

    out: InstanceRecommendations = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.instance_recommendation.deserialize_aws_json_1_0(
                item
            )
        )
    return out
