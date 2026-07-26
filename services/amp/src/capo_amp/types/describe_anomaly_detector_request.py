"""Generated from Smithy shape ``com.amazonaws.amp#DescribeAnomalyDetectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amp.types.anomaly_detector_id
    import capo_amp.types.workspace_id


class DescribeAnomalyDetectorRequest(TypedDict, closed=True):
    workspace_id: "capo_amp.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace containing the anomaly detector.</p>"""
    anomaly_detector_id: "capo_amp.types.anomaly_detector_id.AnomalyDetectorId"
    """<p>The identifier of the anomaly detector to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAnomalyDetectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAnomalyDetectorRequest:
    out: DescribeAnomalyDetectorRequest = {}  # type: ignore[typeddict-item]
    return out
