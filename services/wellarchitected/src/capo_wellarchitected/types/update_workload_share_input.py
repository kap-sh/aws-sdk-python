"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateWorkloadShareInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.permission_type
    import capo_wellarchitected.types.share_id
    import capo_wellarchitected.types.workload_id


class UpdateWorkloadShareInput(TypedDict, closed=True):
    share_id: "capo_wellarchitected.types.share_id.ShareId"
    workload_id: "capo_wellarchitected.types.workload_id.WorkloadId"
    permission_type: NotRequired[
        "capo_wellarchitected.types.permission_type.PermissionType"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkloadShareInput) -> dict:
    out: dict = {}
    if "permission_type" in value:
        import capo_wellarchitected.types.permission_type

        out["PermissionType"] = (
            capo_wellarchitected.types.permission_type.serialize_json(
                value["permission_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateWorkloadShareInput:
    out: UpdateWorkloadShareInput = {}  # type: ignore[typeddict-item]
    if "PermissionType" in data:
        import capo_wellarchitected.types.permission_type

        out["permission_type"] = (
            capo_wellarchitected.types.permission_type.deserialize_json(
                data["PermissionType"]
            )
        )
    return out
