"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetMilestoneInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.milestone_number
    import capo_wellarchitected.types.workload_id


class GetMilestoneInput(TypedDict, closed=True):
    workload_id: "capo_wellarchitected.types.workload_id.WorkloadId"
    milestone_number: "capo_wellarchitected.types.milestone_number.MilestoneNumber"


# --- restJson1 ser/de ---
def serialize_json(value: GetMilestoneInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMilestoneInput:
    out: GetMilestoneInput = {}  # type: ignore[typeddict-item]
    return out
