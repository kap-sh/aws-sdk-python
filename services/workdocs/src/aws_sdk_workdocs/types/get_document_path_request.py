"""Generated from Smithy shape ``com.amazonaws.workdocs#GetDocumentPathRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.field_names_type
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.limit_type
    import aws_sdk_workdocs.types.page_marker_type


class GetDocumentPathRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    document_id: "aws_sdk_workdocs.types.id_type.IdType"
    """<p>The ID of the document.</p>"""
    limit: NotRequired["aws_sdk_workdocs.types.limit_type.LimitType"]
    """<p>The maximum number of levels in the hierarchy to return.</p>"""
    fields: NotRequired["aws_sdk_workdocs.types.field_names_type.FieldNamesType"]
    """<p>A comma-separated list of values. Specify <code>NAME</code> to include the names of the parent folders.</p>"""
    marker: NotRequired["aws_sdk_workdocs.types.page_marker_type.PageMarkerType"]
    """<p>This value is not supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDocumentPathRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDocumentPathRequest:
    out: GetDocumentPathRequest = {}  # type: ignore[typeddict-item]
    return out
