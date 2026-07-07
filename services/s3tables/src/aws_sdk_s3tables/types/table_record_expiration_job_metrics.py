"""Generated from Smithy shape ``com.amazonaws.s3tables#TableRecordExpirationJobMetrics``."""

from typing_extensions import NotRequired, TypedDict


class TableRecordExpirationJobMetrics(TypedDict, closed=True):
    deleted_data_files: NotRequired["int"]
    """<p>The total number of data files that were removed when the job ran.</p>"""
    deleted_records: NotRequired["int"]
    """<p>The total number of records that were removed when the job ran.</p>"""
    removed_files_size: NotRequired["int"]
    """<p>The total size (in bytes) of the data files that were removed when the job ran.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableRecordExpirationJobMetrics) -> dict:
    out: dict = {}
    if "deleted_data_files" in value:
        out["deletedDataFiles"] = value["deleted_data_files"]
    if "deleted_records" in value:
        out["deletedRecords"] = value["deleted_records"]
    if "removed_files_size" in value:
        out["removedFilesSize"] = value["removed_files_size"]
    return out


def deserialize_json(data: dict) -> TableRecordExpirationJobMetrics:
    out: TableRecordExpirationJobMetrics = {}  # type: ignore[typeddict-item]
    if "deletedDataFiles" in data:
        out["deleted_data_files"] = data["deletedDataFiles"]
    if "deletedRecords" in data:
        out["deleted_records"] = data["deletedRecords"]
    if "removedFilesSize" in data:
        out["removed_files_size"] = data["removedFilesSize"]
    return out
