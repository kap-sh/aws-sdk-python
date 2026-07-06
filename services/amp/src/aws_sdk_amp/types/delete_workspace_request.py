"""Generated from Smithy shape ``com.amazonaws.amp#DeleteWorkspaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amp.types.idempotency_token
    import aws_sdk_amp.types.workspace_id


class DeleteWorkspaceRequest(TypedDict, closed=True):
    workspace_id: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to delete.</p>"""
    client_token: NotRequired["aws_sdk_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkspaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkspaceRequest:
    out: DeleteWorkspaceRequest = {}  # type: ignore[typeddict-item]
    return out
