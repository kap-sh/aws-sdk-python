"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateWorkloadShareInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.permission_type
    import aws_sdk_wellarchitected.types.share_id
    import aws_sdk_wellarchitected.types.workload_id


class UpdateWorkloadShareInput(TypedDict):
    share_id: "aws_sdk_wellarchitected.types.share_id.ShareId"
    workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId"
    permission_type: NotRequired[
        "aws_sdk_wellarchitected.types.permission_type.PermissionType"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkloadShareInput) -> dict:
    out: dict = {}
    if "permission_type" in value:
        import aws_sdk_wellarchitected.types.permission_type

        out["PermissionType"] = (
            aws_sdk_wellarchitected.types.permission_type.serialize_json(
                value["permission_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateWorkloadShareInput:
    out: UpdateWorkloadShareInput = {}  # type: ignore[typeddict-item]
    if "PermissionType" in data:
        import aws_sdk_wellarchitected.types.permission_type

        out["permission_type"] = (
            aws_sdk_wellarchitected.types.permission_type.deserialize_json(
                data["PermissionType"]
            )
        )
    return out
