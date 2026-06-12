"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EffectivePreferredResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.effective_preferred_resource

EffectivePreferredResources: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.effective_preferred_resource.EffectivePreferredResource"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EffectivePreferredResources) -> list:
    import aws_sdk_compute_optimizer.types.effective_preferred_resource

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.effective_preferred_resource.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EffectivePreferredResources:
    import aws_sdk_compute_optimizer.types.effective_preferred_resource

    out: EffectivePreferredResources = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.effective_preferred_resource.deserialize_aws_json_1_0(
                item
            )
        )
    return out
