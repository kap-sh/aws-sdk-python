"""Generated from Smithy shape ``com.amazonaws.amp#DeleteAlertManagerDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.idempotency_token
    import capo_amp.types.workspace_id


class DeleteAlertManagerDefinitionRequest(TypedDict, closed=True):
    workspace_id: "capo_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to delete the alert manager definition from.</p>"""
    client_token: NotRequired["capo_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAlertManagerDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAlertManagerDefinitionRequest:
    out: DeleteAlertManagerDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
