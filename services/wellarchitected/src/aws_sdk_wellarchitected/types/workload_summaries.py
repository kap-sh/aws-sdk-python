"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.workload_summary

WorkloadSummaries: TypeAlias = list[
    "aws_sdk_wellarchitected.types.workload_summary.WorkloadSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadSummaries) -> list:
    import aws_sdk_wellarchitected.types.workload_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_wellarchitected.types.workload_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkloadSummaries:
    import aws_sdk_wellarchitected.types.workload_summary

    out: WorkloadSummaries = []
    for item in data:
        out.append(
            aws_sdk_wellarchitected.types.workload_summary.deserialize_json(item)
        )
    return out
