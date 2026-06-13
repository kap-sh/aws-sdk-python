"""Generated from Smithy shape ``com.amazonaws.grafana#DeleteWorkspaceApiKeyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.api_key_name
    import aws_sdk_grafana.types.workspace_id


class DeleteWorkspaceApiKeyResponse(TypedDict):
    key_name: "aws_sdk_grafana.types.api_key_name.ApiKeyName"
    """<p>The name of the key that was deleted.</p>"""
    workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace where the key was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkspaceApiKeyResponse) -> dict:
    out: dict = {}
    out["keyName"] = value["key_name"]
    out["workspaceId"] = value["workspace_id"]
    return out


def deserialize_json(data: dict) -> DeleteWorkspaceApiKeyResponse:
    out: DeleteWorkspaceApiKeyResponse = {}  # type: ignore[typeddict-item]
    if "keyName" in data:
        out["key_name"] = data["keyName"]
    else:
        raise DeserializationError("DeleteWorkspaceApiKeyResponse.key_name required")
    if "workspaceId" in data:
        out["workspace_id"] = data["workspaceId"]
    else:
        raise DeserializationError(
            "DeleteWorkspaceApiKeyResponse.workspace_id required"
        )
    return out
