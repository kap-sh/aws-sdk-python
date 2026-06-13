"""Generated from Smithy shape ``com.amazonaws.amp#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amp.types.idempotency_token
    import aws_sdk_amp.types.workspace_id


class DeleteResourcePolicyRequest(TypedDict):
    workspace_id: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace from which to delete the resource-based policy.</p>"""
    client_token: NotRequired["aws_sdk_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the request is safe to retry (idempotent).</p>"""
    revision_id: NotRequired["str"]
    """<p>The revision ID of the policy to delete. Use this parameter to ensure that you are deleting the correct version of the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
