"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestionJobStatistics``."""

from typing_extensions import TypedDict


class IngestionJobStatistics(TypedDict, closed=True):
    number_of_documents_scanned: "int"
    """<p>The total number of source documents that were scanned. Includes new, updated, and unchanged documents.</p>"""
    number_of_metadata_documents_scanned: "int"
    """<p>The total number of metadata files that were scanned. Includes new, updated, and unchanged files.</p>"""
    number_of_new_documents_indexed: "int"
    """<p>The number of new source documents in the data source that were successfully indexed.</p>"""
    number_of_modified_documents_indexed: "int"
    """<p>The number of modified source documents in the data source that were successfully indexed.</p>"""
    number_of_metadata_documents_modified: "int"
    """<p>The number of metadata files that were updated or deleted.</p>"""
    number_of_documents_deleted: "int"
    """<p>The number of source documents that were deleted.</p>"""
    number_of_documents_failed: "int"
    """<p>The number of source documents that failed to be ingested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestionJobStatistics) -> dict:
    out: dict = {}
    out["numberOfDocumentsScanned"] = value.get("number_of_documents_scanned", 0)
    out["numberOfMetadataDocumentsScanned"] = value.get(
        "number_of_metadata_documents_scanned", 0
    )
    out["numberOfNewDocumentsIndexed"] = value.get("number_of_new_documents_indexed", 0)
    out["numberOfModifiedDocumentsIndexed"] = value.get(
        "number_of_modified_documents_indexed", 0
    )
    out["numberOfMetadataDocumentsModified"] = value.get(
        "number_of_metadata_documents_modified", 0
    )
    out["numberOfDocumentsDeleted"] = value.get("number_of_documents_deleted", 0)
    out["numberOfDocumentsFailed"] = value.get("number_of_documents_failed", 0)
    return out


def deserialize_json(data: dict) -> IngestionJobStatistics:
    out: IngestionJobStatistics = {}  # type: ignore[typeddict-item]
    if data.get("numberOfDocumentsScanned") is not None:
        out["number_of_documents_scanned"] = data["numberOfDocumentsScanned"]
    else:
        out["number_of_documents_scanned"] = 0
    if data.get("numberOfMetadataDocumentsScanned") is not None:
        out["number_of_metadata_documents_scanned"] = data[
            "numberOfMetadataDocumentsScanned"
        ]
    else:
        out["number_of_metadata_documents_scanned"] = 0
    if data.get("numberOfNewDocumentsIndexed") is not None:
        out["number_of_new_documents_indexed"] = data["numberOfNewDocumentsIndexed"]
    else:
        out["number_of_new_documents_indexed"] = 0
    if data.get("numberOfModifiedDocumentsIndexed") is not None:
        out["number_of_modified_documents_indexed"] = data[
            "numberOfModifiedDocumentsIndexed"
        ]
    else:
        out["number_of_modified_documents_indexed"] = 0
    if data.get("numberOfMetadataDocumentsModified") is not None:
        out["number_of_metadata_documents_modified"] = data[
            "numberOfMetadataDocumentsModified"
        ]
    else:
        out["number_of_metadata_documents_modified"] = 0
    if data.get("numberOfDocumentsDeleted") is not None:
        out["number_of_documents_deleted"] = data["numberOfDocumentsDeleted"]
    else:
        out["number_of_documents_deleted"] = 0
    if data.get("numberOfDocumentsFailed") is not None:
        out["number_of_documents_failed"] = data["numberOfDocumentsFailed"]
    else:
        out["number_of_documents_failed"] = 0
    return out
