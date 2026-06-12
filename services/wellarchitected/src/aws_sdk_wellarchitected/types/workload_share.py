"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadShare``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.aws_account_id
    import aws_sdk_wellarchitected.types.permission_type
    import aws_sdk_wellarchitected.types.share_id
    import aws_sdk_wellarchitected.types.share_status
    import aws_sdk_wellarchitected.types.shared_with
    import aws_sdk_wellarchitected.types.workload_id
    import aws_sdk_wellarchitected.types.workload_name


class WorkloadShare(TypedDict):
    share_id: NotRequired["aws_sdk_wellarchitected.types.share_id.ShareId"]
    shared_by: NotRequired["aws_sdk_wellarchitected.types.aws_account_id.AwsAccountId"]
    shared_with: NotRequired["aws_sdk_wellarchitected.types.shared_with.SharedWith"]
    permission_type: NotRequired[
        "aws_sdk_wellarchitected.types.permission_type.PermissionType"
    ]
    status: NotRequired["aws_sdk_wellarchitected.types.share_status.ShareStatus"]
    workload_name: NotRequired[
        "aws_sdk_wellarchitected.types.workload_name.WorkloadName"
    ]
    workload_id: NotRequired["aws_sdk_wellarchitected.types.workload_id.WorkloadId"]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadShare) -> dict:
    out: dict = {}
    if "share_id" in value:
        out["ShareId"] = value["share_id"]
    if "shared_by" in value:
        out["SharedBy"] = value["shared_by"]
    if "shared_with" in value:
        out["SharedWith"] = value["shared_with"]
    if "permission_type" in value:
        import aws_sdk_wellarchitected.types.permission_type

        out["PermissionType"] = (
            aws_sdk_wellarchitected.types.permission_type.serialize_json(
                value["permission_type"]
            )
        )
    if "status" in value:
        import aws_sdk_wellarchitected.types.share_status

        out["Status"] = aws_sdk_wellarchitected.types.share_status.serialize_json(
            value["status"]
        )
    if "workload_name" in value:
        out["WorkloadName"] = value["workload_name"]
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    return out


def deserialize_json(data: dict) -> WorkloadShare:
    out: WorkloadShare = {}  # type: ignore[typeddict-item]
    if "ShareId" in data:
        out["share_id"] = data["ShareId"]
    if "SharedBy" in data:
        out["shared_by"] = data["SharedBy"]
    if "SharedWith" in data:
        out["shared_with"] = data["SharedWith"]
    if "PermissionType" in data:
        import aws_sdk_wellarchitected.types.permission_type

        out["permission_type"] = (
            aws_sdk_wellarchitected.types.permission_type.deserialize_json(
                data["PermissionType"]
            )
        )
    if "Status" in data:
        import aws_sdk_wellarchitected.types.share_status

        out["status"] = aws_sdk_wellarchitected.types.share_status.deserialize_json(
            data["Status"]
        )
    if "WorkloadName" in data:
        out["workload_name"] = data["WorkloadName"]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    return out
