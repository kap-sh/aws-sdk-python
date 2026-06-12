"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleDimensionValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.idle_dimension_value

IdleDimensionValues: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.idle_dimension_value.IdleDimensionValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleDimensionValues) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> IdleDimensionValues:
    return list(data)
