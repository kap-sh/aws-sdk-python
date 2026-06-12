"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleDimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.idle_dimension

IdleDimensions: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.idle_dimension.IdleDimension"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleDimensions) -> list:
    import aws_sdk_compute_optimizer.types.idle_dimension

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.idle_dimension.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> IdleDimensions:
    import aws_sdk_compute_optimizer.types.idle_dimension

    out: IdleDimensions = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.idle_dimension.deserialize_aws_json_1_0(
                item
            )
        )
    return out
