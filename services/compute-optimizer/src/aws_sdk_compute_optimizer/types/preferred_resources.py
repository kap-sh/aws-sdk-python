"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#PreferredResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.preferred_resource

PreferredResources: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.preferred_resource.PreferredResource"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreferredResources) -> list:
    import aws_sdk_compute_optimizer.types.preferred_resource

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.preferred_resource.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PreferredResources:
    import aws_sdk_compute_optimizer.types.preferred_resource

    out: PreferredResources = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.preferred_resource.deserialize_aws_json_1_0(
                item
            )
        )
    return out
