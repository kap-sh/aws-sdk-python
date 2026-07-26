"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListMilestonesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.milestone_summaries
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.workload_id


class ListMilestonesOutput(TypedDict, closed=True):
    workload_id: NotRequired["capo_wellarchitected.types.workload_id.WorkloadId"]
    milestone_summaries: NotRequired[
        "capo_wellarchitected.types.milestone_summaries.MilestoneSummaries"
    ]
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListMilestonesOutput) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "milestone_summaries" in value:
        import capo_wellarchitected.types.milestone_summaries

        out["MilestoneSummaries"] = (
            capo_wellarchitected.types.milestone_summaries.serialize_json(
                value["milestone_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMilestonesOutput:
    out: ListMilestonesOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "MilestoneSummaries" in data:
        import capo_wellarchitected.types.milestone_summaries

        out["milestone_summaries"] = (
            capo_wellarchitected.types.milestone_summaries.deserialize_json(
                data["MilestoneSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
