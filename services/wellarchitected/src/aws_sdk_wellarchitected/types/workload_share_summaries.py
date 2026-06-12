"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadShareSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.workload_share_summary

WorkloadShareSummaries: TypeAlias = list[
    "aws_sdk_wellarchitected.types.workload_share_summary.WorkloadShareSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadShareSummaries) -> list:
    import aws_sdk_wellarchitected.types.workload_share_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_wellarchitected.types.workload_share_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WorkloadShareSummaries:
    import aws_sdk_wellarchitected.types.workload_share_summary

    out: WorkloadShareSummaries = []
    for item in data:
        out.append(
            aws_sdk_wellarchitected.types.workload_share_summary.deserialize_json(item)
        )
    return out
