"""Generated from Smithy shape ``com.amazonaws.grafana#CreateWorkspaceServiceAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.role
    import aws_sdk_grafana.types.workspace_id


class CreateWorkspaceServiceAccountResponse(TypedDict):
    id: "str"
    """<p>The ID of the service account.</p>"""
    name: "str"
    """<p>The name of the service account.</p>"""
    grafana_role: "aws_sdk_grafana.types.role.Role"
    """<p>The permission level given to the service account.</p>"""
    workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId"
    """<p>The workspace with which the service account is associated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceServiceAccountResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["grafanaRole"] = value["grafana_role"]
    out["workspaceId"] = value["workspace_id"]
    return out


def deserialize_json(data: dict) -> CreateWorkspaceServiceAccountResponse:
    out: CreateWorkspaceServiceAccountResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateWorkspaceServiceAccountResponse.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CreateWorkspaceServiceAccountResponse.name required"
        )
    if "grafanaRole" in data:
        out["grafana_role"] = data["grafanaRole"]
    else:
        raise DeserializationError(
            "CreateWorkspaceServiceAccountResponse.grafana_role required"
        )
    if "workspaceId" in data:
        out["workspace_id"] = data["workspaceId"]
    else:
        raise DeserializationError(
            "CreateWorkspaceServiceAccountResponse.workspace_id required"
        )
    return out
