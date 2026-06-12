"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateWorkloadShareInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.client_request_token
    import aws_sdk_wellarchitected.types.permission_type
    import aws_sdk_wellarchitected.types.shared_with
    import aws_sdk_wellarchitected.types.workload_id


class CreateWorkloadShareInput(TypedDict):
    workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId"
    shared_with: NotRequired["aws_sdk_wellarchitected.types.shared_with.SharedWith"]
    permission_type: NotRequired[
        "aws_sdk_wellarchitected.types.permission_type.PermissionType"
    ]
    client_request_token: NotRequired[
        "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkloadShareInput) -> dict:
    out: dict = {}
    if "shared_with" in value:
        out["SharedWith"] = value["shared_with"]
    if "permission_type" in value:
        import aws_sdk_wellarchitected.types.permission_type

        out["PermissionType"] = (
            aws_sdk_wellarchitected.types.permission_type.serialize_json(
                value["permission_type"]
            )
        )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateWorkloadShareInput:
    out: CreateWorkloadShareInput = {}  # type: ignore[typeddict-item]
    if "SharedWith" in data:
        out["shared_with"] = data["SharedWith"]
    if "PermissionType" in data:
        import aws_sdk_wellarchitected.types.permission_type

        out["permission_type"] = (
            aws_sdk_wellarchitected.types.permission_type.deserialize_json(
                data["PermissionType"]
            )
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
