"""Generated from Smithy shape ``com.amazonaws.grafana#CreateWorkspaceApiKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import capo_grafana.types.api_key_name
    import capo_grafana.types.workspace_id


class CreateWorkspaceApiKeyRequest(TypedDict, closed=True):
    key_name: "capo_grafana.types.api_key_name.ApiKeyName"
    """<p>Specifies the name of the key. Keynames must be unique to the workspace.</p>"""
    key_role: "str"
    """<p>Specifies the permission level of the key.</p> <p> Valid values: <code>ADMIN</code>|<code>EDITOR</code>|<code>VIEWER</code> </p>"""
    seconds_to_live: "int"
    """<p>Specifies the time in seconds until the key expires. Keys can be valid for up to 30 days.</p>"""
    workspace_id: "capo_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to create an API key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceApiKeyRequest) -> dict:
    out: dict = {}
    out["keyName"] = value["key_name"]
    out["keyRole"] = value["key_role"]
    out["secondsToLive"] = value["seconds_to_live"]
    return out


def deserialize_json(data: dict) -> CreateWorkspaceApiKeyRequest:
    out: CreateWorkspaceApiKeyRequest = {}  # type: ignore[typeddict-item]
    if "keyName" in data:
        out["key_name"] = data["keyName"]
    else:
        raise DeserializationError("CreateWorkspaceApiKeyRequest.key_name required")
    if "keyRole" in data:
        out["key_role"] = data["keyRole"]
    else:
        raise DeserializationError("CreateWorkspaceApiKeyRequest.key_role required")
    if "secondsToLive" in data:
        out["seconds_to_live"] = data["secondsToLive"]
    else:
        raise DeserializationError(
            "CreateWorkspaceApiKeyRequest.seconds_to_live required"
        )
    return out
