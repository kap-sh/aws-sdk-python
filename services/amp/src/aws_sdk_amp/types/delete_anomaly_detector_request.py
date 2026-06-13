"""Generated from Smithy shape ``com.amazonaws.amp#DeleteAnomalyDetectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amp.types.anomaly_detector_id
    import aws_sdk_amp.types.idempotency_token
    import aws_sdk_amp.types.workspace_id


class DeleteAnomalyDetectorRequest(TypedDict):
    workspace_id: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace containing the anomaly detector to delete.</p>"""
    anomaly_detector_id: "aws_sdk_amp.types.anomaly_detector_id.AnomalyDetectorId"
    """<p>The identifier of the anomaly detector to delete.</p>"""
    client_token: NotRequired["aws_sdk_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAnomalyDetectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAnomalyDetectorRequest:
    out: DeleteAnomalyDetectorRequest = {}  # type: ignore[typeddict-item]
    return out
