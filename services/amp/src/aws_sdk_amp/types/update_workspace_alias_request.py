"""Generated from Smithy shape ``com.amazonaws.amp#UpdateWorkspaceAliasRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amp.types.idempotency_token
    import aws_sdk_amp.types.workspace_alias
    import aws_sdk_amp.types.workspace_id


class UpdateWorkspaceAliasRequest(TypedDict):
    workspace_id: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to update.</p>"""
    alias: NotRequired["aws_sdk_amp.types.workspace_alias.WorkspaceAlias"]
    """<p>The new alias for the workspace. It does not need to be unique.</p> <p>Amazon Managed Service for Prometheus will automatically strip any blank spaces from the beginning and end of the alias that you specify.</p>"""
    client_token: NotRequired["aws_sdk_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceAliasRequest) -> dict:
    out: dict = {}
    if "alias" in value:
        out["alias"] = value["alias"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateWorkspaceAliasRequest:
    out: UpdateWorkspaceAliasRequest = {}  # type: ignore[typeddict-item]
    if "alias" in data:
        out["alias"] = data["alias"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
