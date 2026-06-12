"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetMilestoneInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.milestone_number
    import aws_sdk_wellarchitected.types.workload_id


class GetMilestoneInput(TypedDict):
    workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId"
    milestone_number: "aws_sdk_wellarchitected.types.milestone_number.MilestoneNumber"


# --- restJson1 ser/de ---
def serialize_json(value: GetMilestoneInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMilestoneInput:
    out: GetMilestoneInput = {}  # type: ignore[typeddict-item]
    return out
