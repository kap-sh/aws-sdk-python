"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateWorkloadOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.workload_arn
    import capo_wellarchitected.types.workload_id


class CreateWorkloadOutput(TypedDict, closed=True):
    workload_id: NotRequired["capo_wellarchitected.types.workload_id.WorkloadId"]
    workload_arn: NotRequired["capo_wellarchitected.types.workload_arn.WorkloadArn"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkloadOutput) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "workload_arn" in value:
        out["WorkloadArn"] = value["workload_arn"]
    return out


def deserialize_json(data: dict) -> CreateWorkloadOutput:
    out: CreateWorkloadOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "WorkloadArn" in data:
        out["workload_arn"] = data["WorkloadArn"]
    return out
