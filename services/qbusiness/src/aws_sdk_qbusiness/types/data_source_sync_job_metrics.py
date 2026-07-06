"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataSourceSyncJobMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.metric_value


class DataSourceSyncJobMetrics(TypedDict, closed=True):
    documents_added: NotRequired["aws_sdk_qbusiness.types.metric_value.MetricValue"]
    """<p>The current count of documents added from the data source during the data source sync.</p>"""
    documents_modified: NotRequired["aws_sdk_qbusiness.types.metric_value.MetricValue"]
    """<p>The current count of documents modified in the data source during the data source sync.</p>"""
    documents_deleted: NotRequired["aws_sdk_qbusiness.types.metric_value.MetricValue"]
    """<p>The current count of documents deleted from the data source during the data source sync.</p>"""
    documents_failed: NotRequired["aws_sdk_qbusiness.types.metric_value.MetricValue"]
    """<p>The current count of documents that failed to sync from the data source during the data source sync.</p>"""
    documents_scanned: NotRequired["aws_sdk_qbusiness.types.metric_value.MetricValue"]
    """<p>The current count of documents crawled by the ongoing sync job in the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceSyncJobMetrics) -> dict:
    out: dict = {}
    if "documents_added" in value:
        out["documentsAdded"] = value["documents_added"]
    if "documents_modified" in value:
        out["documentsModified"] = value["documents_modified"]
    if "documents_deleted" in value:
        out["documentsDeleted"] = value["documents_deleted"]
    if "documents_failed" in value:
        out["documentsFailed"] = value["documents_failed"]
    if "documents_scanned" in value:
        out["documentsScanned"] = value["documents_scanned"]
    return out


def deserialize_json(data: dict) -> DataSourceSyncJobMetrics:
    out: DataSourceSyncJobMetrics = {}  # type: ignore[typeddict-item]
    if "documentsAdded" in data:
        out["documents_added"] = data["documentsAdded"]
    if "documentsModified" in data:
        out["documents_modified"] = data["documentsModified"]
    if "documentsDeleted" in data:
        out["documents_deleted"] = data["documentsDeleted"]
    if "documentsFailed" in data:
        out["documents_failed"] = data["documentsFailed"]
    if "documentsScanned" in data:
        out["documents_scanned"] = data["documentsScanned"]
    return out
