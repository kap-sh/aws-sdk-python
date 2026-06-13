"""Generated from Smithy shape ``com.amazonaws.grafana#DeleteWorkspaceApiKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_grafana.types.api_key_name
    import aws_sdk_grafana.types.workspace_id


class DeleteWorkspaceApiKeyRequest(TypedDict):
    key_name: "aws_sdk_grafana.types.api_key_name.ApiKeyName"
    """<p>The name of the API key to delete.</p>"""
    workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkspaceApiKeyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkspaceApiKeyRequest:
    out: DeleteWorkspaceApiKeyRequest = {}  # type: ignore[typeddict-item]
    return out
