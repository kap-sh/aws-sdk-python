"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.workload_summary

WorkloadSummaries: TypeAlias = list[
    "capo_wellarchitected.types.workload_summary.WorkloadSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadSummaries) -> list:
    import capo_wellarchitected.types.workload_summary

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.workload_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkloadSummaries:
    import capo_wellarchitected.types.workload_summary

    out: WorkloadSummaries = []
    for item in data:
        out.append(capo_wellarchitected.types.workload_summary.deserialize_json(item))
    return out
