"""Generated from Smithy shape ``com.amazonaws.grafana#CreateWorkspaceApiKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.api_key_name
    import aws_sdk_grafana.types.api_key_token
    import aws_sdk_grafana.types.workspace_id


class CreateWorkspaceApiKeyResponse(TypedDict, closed=True):
    key_name: "aws_sdk_grafana.types.api_key_name.ApiKeyName"
    """<p>The name of the key that was created.</p>"""
    key: "aws_sdk_grafana.types.api_key_token.ApiKeyToken"
    """<p>The key token. Use this value as a bearer token to authenticate HTTP requests to the workspace.</p>"""
    workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace that the key is valid for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceApiKeyResponse) -> dict:
    out: dict = {}
    out["keyName"] = value["key_name"]
    out["key"] = value["key"]
    out["workspaceId"] = value["workspace_id"]
    return out


def deserialize_json(data: dict) -> CreateWorkspaceApiKeyResponse:
    out: CreateWorkspaceApiKeyResponse = {}  # type: ignore[typeddict-item]
    if "keyName" in data:
        out["key_name"] = data["keyName"]
    else:
        raise DeserializationError("CreateWorkspaceApiKeyResponse.key_name required")
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("CreateWorkspaceApiKeyResponse.key required")
    if "workspaceId" in data:
        out["workspace_id"] = data["workspaceId"]
    else:
        raise DeserializationError(
            "CreateWorkspaceApiKeyResponse.workspace_id required"
        )
    return out
