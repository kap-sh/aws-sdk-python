"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceSyncJobMetrics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.metric_value


class DataSourceSyncJobMetrics(TypedDict):
    documents_added: NotRequired["aws_sdk_kendra.types.metric_value.MetricValue"]
    """<p>The number of documents added from the data source up to now in the data source sync.</p>"""
    documents_modified: NotRequired["aws_sdk_kendra.types.metric_value.MetricValue"]
    """<p>The number of documents modified in the data source up to now in the data source sync run.</p>"""
    documents_deleted: NotRequired["aws_sdk_kendra.types.metric_value.MetricValue"]
    """<p>The number of documents deleted from the data source up to now in the data source sync run.</p>"""
    documents_failed: NotRequired["aws_sdk_kendra.types.metric_value.MetricValue"]
    """<p>The number of documents that failed to sync from the data source up to now in the data source sync run.</p>"""
    documents_scanned: NotRequired["aws_sdk_kendra.types.metric_value.MetricValue"]
    """<p>The current number of documents crawled by the current sync job in the data source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceSyncJobMetrics) -> dict:
    out: dict = {}
    if "documents_added" in value:
        out["DocumentsAdded"] = value["documents_added"]
    if "documents_modified" in value:
        out["DocumentsModified"] = value["documents_modified"]
    if "documents_deleted" in value:
        out["DocumentsDeleted"] = value["documents_deleted"]
    if "documents_failed" in value:
        out["DocumentsFailed"] = value["documents_failed"]
    if "documents_scanned" in value:
        out["DocumentsScanned"] = value["documents_scanned"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataSourceSyncJobMetrics:
    out: DataSourceSyncJobMetrics = {}  # type: ignore[typeddict-item]
    if "DocumentsAdded" in data:
        out["documents_added"] = data["DocumentsAdded"]
    if "DocumentsModified" in data:
        out["documents_modified"] = data["DocumentsModified"]
    if "DocumentsDeleted" in data:
        out["documents_deleted"] = data["DocumentsDeleted"]
    if "DocumentsFailed" in data:
        out["documents_failed"] = data["DocumentsFailed"]
    if "DocumentsScanned" in data:
        out["documents_scanned"] = data["DocumentsScanned"]
    return out
