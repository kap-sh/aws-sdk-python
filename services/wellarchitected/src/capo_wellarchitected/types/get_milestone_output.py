"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetMilestoneOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.milestone
    import capo_wellarchitected.types.workload_id


class GetMilestoneOutput(TypedDict, closed=True):
    workload_id: NotRequired["capo_wellarchitected.types.workload_id.WorkloadId"]
    milestone: NotRequired["capo_wellarchitected.types.milestone.Milestone"]


# --- restJson1 ser/de ---
def serialize_json(value: GetMilestoneOutput) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "milestone" in value:
        import capo_wellarchitected.types.milestone

        out["Milestone"] = capo_wellarchitected.types.milestone.serialize_json(
            value["milestone"]
        )
    return out


def deserialize_json(data: dict) -> GetMilestoneOutput:
    out: GetMilestoneOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "Milestone" in data:
        import capo_wellarchitected.types.milestone

        out["milestone"] = capo_wellarchitected.types.milestone.deserialize_json(
            data["Milestone"]
        )
    return out
