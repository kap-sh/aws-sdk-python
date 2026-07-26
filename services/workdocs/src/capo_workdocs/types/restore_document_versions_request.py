"""Generated from Smithy shape ``com.amazonaws.workdocs#RestoreDocumentVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.resource_id_type


class RestoreDocumentVersionsRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    document_id: "capo_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreDocumentVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RestoreDocumentVersionsRequest:
    out: RestoreDocumentVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
