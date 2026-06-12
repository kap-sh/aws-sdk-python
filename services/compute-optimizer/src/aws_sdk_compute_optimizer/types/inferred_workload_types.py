"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InferredWorkloadTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.inferred_workload_type

InferredWorkloadTypes: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.inferred_workload_type.InferredWorkloadType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InferredWorkloadTypes) -> list:
    import aws_sdk_compute_optimizer.types.inferred_workload_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.inferred_workload_type.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InferredWorkloadTypes:
    import aws_sdk_compute_optimizer.types.inferred_workload_type

    out: InferredWorkloadTypes = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.inferred_workload_type.deserialize_aws_json_1_0(
                item
            )
        )
    return out
