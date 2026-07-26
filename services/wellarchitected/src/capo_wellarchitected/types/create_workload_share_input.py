"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateWorkloadShareInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.client_request_token
    import capo_wellarchitected.types.permission_type
    import capo_wellarchitected.types.shared_with
    import capo_wellarchitected.types.workload_id


class CreateWorkloadShareInput(TypedDict, closed=True):
    workload_id: "capo_wellarchitected.types.workload_id.WorkloadId"
    shared_with: NotRequired["capo_wellarchitected.types.shared_with.SharedWith"]
    permission_type: NotRequired[
        "capo_wellarchitected.types.permission_type.PermissionType"
    ]
    client_request_token: NotRequired[
        "capo_wellarchitected.types.client_request_token.ClientRequestToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkloadShareInput) -> dict:
    out: dict = {}
    if "shared_with" in value:
        out["SharedWith"] = value["shared_with"]
    if "permission_type" in value:
        import capo_wellarchitected.types.permission_type

        out["PermissionType"] = (
            capo_wellarchitected.types.permission_type.serialize_json(
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
        import capo_wellarchitected.types.permission_type

        out["permission_type"] = (
            capo_wellarchitected.types.permission_type.deserialize_json(
                data["PermissionType"]
            )
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
