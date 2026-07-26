"""Generated from Smithy shape ``com.amazonaws.grafana#DeleteWorkspaceServiceAccountTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.workspace_id


class DeleteWorkspaceServiceAccountTokenRequest(TypedDict, closed=True):
    token_id: "str"
    """<p>The ID of the token to delete.</p>"""
    service_account_id: "str"
    """<p>The ID of the service account from which to delete the token.</p>"""
    workspace_id: "capo_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace from which to delete the token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkspaceServiceAccountTokenRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkspaceServiceAccountTokenRequest:
    out: DeleteWorkspaceServiceAccountTokenRequest = {}  # type: ignore[typeddict-item]
    return out
