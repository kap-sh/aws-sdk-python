"""Generated from Smithy shape ``com.amazonaws.amp#DeleteLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amp.types.idempotency_token
    import aws_sdk_amp.types.workspace_id


class DeleteLoggingConfigurationRequest(TypedDict):
    workspace_id: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace containing the logging configuration to delete.</p>"""
    client_token: NotRequired["aws_sdk_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLoggingConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteLoggingConfigurationRequest:
    out: DeleteLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
