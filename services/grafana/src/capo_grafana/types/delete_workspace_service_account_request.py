"""Generated from Smithy shape ``com.amazonaws.grafana#DeleteWorkspaceServiceAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.workspace_id


class DeleteWorkspaceServiceAccountRequest(TypedDict, closed=True):
    service_account_id: "str"
    """<p>The ID of the service account to delete.</p>"""
    workspace_id: "capo_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace where the service account resides.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkspaceServiceAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkspaceServiceAccountRequest:
    out: DeleteWorkspaceServiceAccountRequest = {}  # type: ignore[typeddict-item]
    return out
