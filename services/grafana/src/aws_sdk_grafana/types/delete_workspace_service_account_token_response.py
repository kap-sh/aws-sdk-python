"""Generated from Smithy shape ``com.amazonaws.grafana#DeleteWorkspaceServiceAccountTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.workspace_id


class DeleteWorkspaceServiceAccountTokenResponse(TypedDict, closed=True):
    token_id: "str"
    """<p>The ID of the token that was deleted.</p>"""
    service_account_id: "str"
    """<p>The ID of the service account where the token was deleted.</p>"""
    workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace where the token was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkspaceServiceAccountTokenResponse) -> dict:
    out: dict = {}
    out["tokenId"] = value["token_id"]
    out["serviceAccountId"] = value["service_account_id"]
    out["workspaceId"] = value["workspace_id"]
    return out


def deserialize_json(data: dict) -> DeleteWorkspaceServiceAccountTokenResponse:
    out: DeleteWorkspaceServiceAccountTokenResponse = {}  # type: ignore[typeddict-item]
    if "tokenId" in data:
        out["token_id"] = data["tokenId"]
    else:
        raise DeserializationError(
            "DeleteWorkspaceServiceAccountTokenResponse.token_id required"
        )
    if "serviceAccountId" in data:
        out["service_account_id"] = data["serviceAccountId"]
    else:
        raise DeserializationError(
            "DeleteWorkspaceServiceAccountTokenResponse.service_account_id required"
        )
    if "workspaceId" in data:
        out["workspace_id"] = data["workspaceId"]
    else:
        raise DeserializationError(
            "DeleteWorkspaceServiceAccountTokenResponse.workspace_id required"
        )
    return out
