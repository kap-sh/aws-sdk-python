"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateMilestoneOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.milestone_number
    import capo_wellarchitected.types.workload_id


class CreateMilestoneOutput(TypedDict, closed=True):
    workload_id: NotRequired["capo_wellarchitected.types.workload_id.WorkloadId"]
    milestone_number: NotRequired[
        "capo_wellarchitected.types.milestone_number.MilestoneNumber"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateMilestoneOutput) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "milestone_number" in value:
        out["MilestoneNumber"] = value["milestone_number"]
    return out


def deserialize_json(data: dict) -> CreateMilestoneOutput:
    out: CreateMilestoneOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "MilestoneNumber" in data:
        out["milestone_number"] = data["MilestoneNumber"]
    return out
