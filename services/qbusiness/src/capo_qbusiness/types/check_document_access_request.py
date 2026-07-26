"""Generated from Smithy shape ``com.amazonaws.qbusiness#CheckDocumentAccessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.data_source_id
    import capo_qbusiness.types.document_id
    import capo_qbusiness.types.index_id
    import capo_qbusiness.types.string


class CheckDocumentAccessRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier of the application. This is required to identify the specific Amazon Q Business application context for the document access check.</p>"""
    index_id: "capo_qbusiness.types.index_id.IndexId"
    """<p>The unique identifier of the index. Used to locate the correct index within the application where the document is stored.</p>"""
    user_id: "capo_qbusiness.types.string.String"
    """<p>The unique identifier of the user. Used to check the access permissions for this specific user against the document's ACL.</p>"""
    document_id: "capo_qbusiness.types.document_id.DocumentId"
    """<p>The unique identifier of the document. Specifies which document's access permissions are being checked.</p>"""
    data_source_id: NotRequired["capo_qbusiness.types.data_source_id.DataSourceId"]
    """<p>The unique identifier of the data source. Identifies the specific data source from which the document originates. Should not be used when a document is uploaded directly with BatchPutDocument, as no dataSourceId is available or necessary. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CheckDocumentAccessRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CheckDocumentAccessRequest:
    out: CheckDocumentAccessRequest = {}  # type: ignore[typeddict-item]
    return out
