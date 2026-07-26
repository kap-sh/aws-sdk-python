"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateWorkloadShareOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.share_id
    import capo_wellarchitected.types.workload_id


class CreateWorkloadShareOutput(TypedDict, closed=True):
    workload_id: NotRequired["capo_wellarchitected.types.workload_id.WorkloadId"]
    share_id: NotRequired["capo_wellarchitected.types.share_id.ShareId"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkloadShareOutput) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "share_id" in value:
        out["ShareId"] = value["share_id"]
    return out


def deserialize_json(data: dict) -> CreateWorkloadShareOutput:
    out: CreateWorkloadShareOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "ShareId" in data:
        out["share_id"] = data["ShareId"]
    return out
