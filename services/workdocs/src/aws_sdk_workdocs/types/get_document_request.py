"""Generated from Smithy shape ``com.amazonaws.workdocs#GetDocumentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.boolean_type
    import aws_sdk_workdocs.types.resource_id_type


class GetDocumentRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    document_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the document.</p>"""
    include_custom_metadata: "aws_sdk_workdocs.types.boolean_type.BooleanType"
    """<p>Set this to <code>TRUE</code> to include custom metadata in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDocumentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDocumentRequest:
    out: GetDocumentRequest = {}  # type: ignore[typeddict-item]
    return out
