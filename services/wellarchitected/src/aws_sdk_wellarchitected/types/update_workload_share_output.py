"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateWorkloadShareOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.workload_id
    import aws_sdk_wellarchitected.types.workload_share


class UpdateWorkloadShareOutput(TypedDict):
    workload_id: NotRequired["aws_sdk_wellarchitected.types.workload_id.WorkloadId"]
    workload_share: NotRequired[
        "aws_sdk_wellarchitected.types.workload_share.WorkloadShare"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkloadShareOutput) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "workload_share" in value:
        import aws_sdk_wellarchitected.types.workload_share

        out["WorkloadShare"] = (
            aws_sdk_wellarchitected.types.workload_share.serialize_json(
                value["workload_share"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateWorkloadShareOutput:
    out: UpdateWorkloadShareOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "WorkloadShare" in data:
        import aws_sdk_wellarchitected.types.workload_share

        out["workload_share"] = (
            aws_sdk_wellarchitected.types.workload_share.deserialize_json(
                data["WorkloadShare"]
            )
        )
    return out
