"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#PreferredResourceValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.preferred_resource_value

PreferredResourceValues: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.preferred_resource_value.PreferredResourceValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreferredResourceValues) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> PreferredResourceValues:
    return list(data)
