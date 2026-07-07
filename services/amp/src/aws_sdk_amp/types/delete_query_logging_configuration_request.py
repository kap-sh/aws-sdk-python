"""Generated from Smithy shape ``com.amazonaws.amp#DeleteQueryLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amp.types.idempotency_token
    import aws_sdk_amp.types.workspace_id


class DeleteQueryLoggingConfigurationRequest(TypedDict, closed=True):
    workspace_id: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace from which to delete the query logging configuration.</p>"""
    client_token: NotRequired["aws_sdk_amp.types.idempotency_token.IdempotencyToken"]
    """<p>(Optional) A unique, case-sensitive identifier that you can provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQueryLoggingConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteQueryLoggingConfigurationRequest:
    out: DeleteQueryLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
