"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InferredWorkloadSavings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.inferred_workload_saving

InferredWorkloadSavings: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.inferred_workload_saving.InferredWorkloadSaving"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InferredWorkloadSavings) -> list:
    import aws_sdk_compute_optimizer.types.inferred_workload_saving

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.inferred_workload_saving.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InferredWorkloadSavings:
    import aws_sdk_compute_optimizer.types.inferred_workload_saving

    out: InferredWorkloadSavings = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.inferred_workload_saving.deserialize_aws_json_1_0(
                item
            )
        )
    return out
