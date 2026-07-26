"""Generated from Smithy shape ``com.amazonaws.grafana#DeleteWorkspaceServiceAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import capo_grafana.types.workspace_id


class DeleteWorkspaceServiceAccountResponse(TypedDict, closed=True):
    service_account_id: "str"
    """<p>The ID of the service account deleted.</p>"""
    workspace_id: "capo_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace where the service account was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkspaceServiceAccountResponse) -> dict:
    out: dict = {}
    out["serviceAccountId"] = value["service_account_id"]
    out["workspaceId"] = value["workspace_id"]
    return out


def deserialize_json(data: dict) -> DeleteWorkspaceServiceAccountResponse:
    out: DeleteWorkspaceServiceAccountResponse = {}  # type: ignore[typeddict-item]
    if "serviceAccountId" in data:
        out["service_account_id"] = data["serviceAccountId"]
    else:
        raise DeserializationError(
            "DeleteWorkspaceServiceAccountResponse.service_account_id required"
        )
    if "workspaceId" in data:
        out["workspace_id"] = data["workspaceId"]
    else:
        raise DeserializationError(
            "DeleteWorkspaceServiceAccountResponse.workspace_id required"
        )
    return out
