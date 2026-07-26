"""Generated from Smithy shape ``com.amazonaws.grafana#DeleteWorkspaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.workspace_id


class DeleteWorkspaceRequest(TypedDict, closed=True):
    workspace_id: "capo_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkspaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkspaceRequest:
    out: DeleteWorkspaceRequest = {}  # type: ignore[typeddict-item]
    return out
