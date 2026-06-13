"""Generated from Smithy shape ``com.amazonaws.amp#ListAnomalyDetectorsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amp.types.anomaly_detector_alias
    import aws_sdk_amp.types.pagination_token
    import aws_sdk_amp.types.workspace_id


class ListAnomalyDetectorsRequest(TypedDict):
    workspace_id: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace containing the anomaly detectors to list.</p>"""
    alias: NotRequired["aws_sdk_amp.types.anomaly_detector_alias.AnomalyDetectorAlias"]
    """<p>Filters the results to anomaly detectors with the specified alias.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single call. Valid range is 1 to 1000.</p>"""
    next_token: NotRequired["aws_sdk_amp.types.pagination_token.PaginationToken"]
    """<p>The pagination token to continue retrieving results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnomalyDetectorsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAnomalyDetectorsRequest:
    out: ListAnomalyDetectorsRequest = {}  # type: ignore[typeddict-item]
    return out
