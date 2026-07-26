"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateWorkloadShareOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.workload_id
    import capo_wellarchitected.types.workload_share


class UpdateWorkloadShareOutput(TypedDict, closed=True):
    workload_id: NotRequired["capo_wellarchitected.types.workload_id.WorkloadId"]
    workload_share: NotRequired[
        "capo_wellarchitected.types.workload_share.WorkloadShare"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkloadShareOutput) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "workload_share" in value:
        import capo_wellarchitected.types.workload_share

        out["WorkloadShare"] = capo_wellarchitected.types.workload_share.serialize_json(
            value["workload_share"]
        )
    return out


def deserialize_json(data: dict) -> UpdateWorkloadShareOutput:
    out: UpdateWorkloadShareOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "WorkloadShare" in data:
        import capo_wellarchitected.types.workload_share

        out["workload_share"] = (
            capo_wellarchitected.types.workload_share.deserialize_json(
                data["WorkloadShare"]
            )
        )
    return out
