"""Generated from Smithy shape ``com.amazonaws.qbusiness#FailedDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.data_source_id
    import capo_qbusiness.types.document_id
    import capo_qbusiness.types.error_detail


class FailedDocument(TypedDict, closed=True):
    id: NotRequired["capo_qbusiness.types.document_id.DocumentId"]
    """<p>The identifier of the document that couldn't be removed from the Amazon Q Business index.</p>"""
    error: NotRequired["capo_qbusiness.types.error_detail.ErrorDetail"]
    """<p>An explanation for why the document couldn't be removed from the index.</p>"""
    data_source_id: NotRequired["capo_qbusiness.types.data_source_id.DataSourceId"]
    """<p>The identifier of the Amazon Q Business data source connector that contains the failed document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedDocument) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "error" in value:
        import capo_qbusiness.types.error_detail

        out["error"] = capo_qbusiness.types.error_detail.serialize_json(value["error"])
    if "data_source_id" in value:
        out["dataSourceId"] = value["data_source_id"]
    return out


def deserialize_json(data: dict) -> FailedDocument:
    out: FailedDocument = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "error" in data:
        import capo_qbusiness.types.error_detail

        out["error"] = capo_qbusiness.types.error_detail.deserialize_json(data["error"])
    if "dataSourceId" in data:
        out["data_source_id"] = data["dataSourceId"]
    return out
