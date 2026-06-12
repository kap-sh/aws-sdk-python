"""Generated from Smithy shape ``com.amazonaws.grafana#CreateWorkspaceServiceAccountTokenResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_grafana.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_grafana.types.service_account_token_summary_with_key
    import aws_sdk_grafana.types.workspace_id

class CreateWorkspaceServiceAccountTokenResponse(TypedDict):
    service_account_token: "aws_sdk_grafana.types.service_account_token_summary_with_key.ServiceAccountTokenSummaryWithKey"
    """<p>Information about the created token, including the key. Be sure to store the key securely.</p>"""
    service_account_id: "str"
    """<p>The ID of the service account where the token was created.</p>"""
    workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace where the token was created.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceServiceAccountTokenResponse) -> dict:
    out: dict = {}
    import aws_sdk_grafana.types.service_account_token_summary_with_key
    out["serviceAccountToken"] = aws_sdk_grafana.types.service_account_token_summary_with_key.serialize_json(value["service_account_token"])
    out["serviceAccountId"] = value["service_account_id"]
    out["workspaceId"] = value["workspace_id"]
    return out


def deserialize_json(data: dict) -> CreateWorkspaceServiceAccountTokenResponse:
    out: CreateWorkspaceServiceAccountTokenResponse = {}  # type: ignore[typeddict-item]
    if "serviceAccountToken" in data:
        import aws_sdk_grafana.types.service_account_token_summary_with_key
        out["service_account_token"] = aws_sdk_grafana.types.service_account_token_summary_with_key.deserialize_json(data["serviceAccountToken"])
    else:
        raise DeserializationError("CreateWorkspaceServiceAccountTokenResponse.service_account_token required")
    if "serviceAccountId" in data:
        out["service_account_id"] = data["serviceAccountId"]
    else:
        raise DeserializationError("CreateWorkspaceServiceAccountTokenResponse.service_account_id required")
    if "workspaceId" in data:
        out["workspace_id"] = data["workspaceId"]
    else:
        raise DeserializationError("CreateWorkspaceServiceAccountTokenResponse.workspace_id required")
    return out