"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListWorkloadsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.workload_summaries


class ListWorkloadsOutput(TypedDict, closed=True):
    workload_summaries: NotRequired[
        "capo_wellarchitected.types.workload_summaries.WorkloadSummaries"
    ]
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkloadsOutput) -> dict:
    out: dict = {}
    if "workload_summaries" in value:
        import capo_wellarchitected.types.workload_summaries

        out["WorkloadSummaries"] = (
            capo_wellarchitected.types.workload_summaries.serialize_json(
                value["workload_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkloadsOutput:
    out: ListWorkloadsOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadSummaries" in data:
        import capo_wellarchitected.types.workload_summaries

        out["workload_summaries"] = (
            capo_wellarchitected.types.workload_summaries.deserialize_json(
                data["WorkloadSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
