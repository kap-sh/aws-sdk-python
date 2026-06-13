"""Generated from Smithy shape ``com.amazonaws.grafana#CreateWorkspaceServiceAccountTokenRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.service_account_token_name
    import aws_sdk_grafana.types.workspace_id


class CreateWorkspaceServiceAccountTokenRequest(TypedDict):
    name: "aws_sdk_grafana.types.service_account_token_name.ServiceAccountTokenName"
    """<p>A name for the token to create.</p>"""
    seconds_to_live: "int"
    """<p>Sets how long the token will be valid, in seconds. You can set the time up to 30 days in the future.</p>"""
    service_account_id: "str"
    """<p>The ID of the service account for which to create a token.</p>"""
    workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace the service account resides within.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceServiceAccountTokenRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["secondsToLive"] = value["seconds_to_live"]
    return out


def deserialize_json(data: dict) -> CreateWorkspaceServiceAccountTokenRequest:
    out: CreateWorkspaceServiceAccountTokenRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CreateWorkspaceServiceAccountTokenRequest.name required"
        )
    if "secondsToLive" in data:
        out["seconds_to_live"] = data["secondsToLive"]
    else:
        raise DeserializationError(
            "CreateWorkspaceServiceAccountTokenRequest.seconds_to_live required"
        )
    return out
