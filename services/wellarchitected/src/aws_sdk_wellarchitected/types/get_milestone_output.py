"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetMilestoneOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.milestone
    import aws_sdk_wellarchitected.types.workload_id


class GetMilestoneOutput(TypedDict):
    workload_id: NotRequired["aws_sdk_wellarchitected.types.workload_id.WorkloadId"]
    milestone: NotRequired["aws_sdk_wellarchitected.types.milestone.Milestone"]


# --- restJson1 ser/de ---
def serialize_json(value: GetMilestoneOutput) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "milestone" in value:
        import aws_sdk_wellarchitected.types.milestone

        out["Milestone"] = aws_sdk_wellarchitected.types.milestone.serialize_json(
            value["milestone"]
        )
    return out


def deserialize_json(data: dict) -> GetMilestoneOutput:
    out: GetMilestoneOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "Milestone" in data:
        import aws_sdk_wellarchitected.types.milestone

        out["milestone"] = aws_sdk_wellarchitected.types.milestone.deserialize_json(
            data["Milestone"]
        )
    return out
